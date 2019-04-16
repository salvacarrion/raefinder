var editor = null;
var rules =  {
 1: ['d', 't'],
 2: ['n', 'ñ', 'y'],
 3: ['m', 'w'],
 4: ['c', 'h', 'k', 'q'],
 5: ['l', 'v', 'll'],
 6: ['s', 'z'],
 7: ['f', 'j'],
 8: ['g', 'x', 'ch'],
 9: ['b', 'p'],
 0: ['r', 'rr']
};

// Default loading
$(document).ready(function() {
  get_cookie_rules()

    // Create JSON editor
    var container = document.getElementById("jsoneditor");
    var options = {};
    editor = new JSONEditor(container, options);
  });


function get_cookie_rules(){
    // Check if cookie 'rules' exists
    if (!!Cookies.get('rules')) {
    } else { // Set default rules
      Cookies.set('rules', JSON.stringify(rules));
    }

    return Cookies.get('rules');
  }

// Set rules in a cookie
function set_rules_in_cookie(new_rules){
  try {
        // var rules = JSON.parse(new_rules);  // Maybe not needed. (JSON editor)
        Cookies.set('rules', JSON.stringify(new_rules));
        return true;
      } catch (e) {
        alert("El formato no es válido");
      }
      return false;
    }

// Save rules [Button]
$('#save-rules').click(function(e){
    // if(set_rules($("#mnemotechnic-rules").val())){
      if(set_rules_in_cookie(editor.get())){ 
        $("#rulesModal").modal('hide');
      }
    });


// Rules modal [OPEN]
$('#rulesModal').on('shown.bs.modal', function (e) {
    // Set rules 
    // $("#mnemotechnic-rules").val(JSON.stringify(Cookies.get('rules')));
    editor.set(JSON.parse(get_cookie_rules()));
  });

// Search number text [Enter key]
$("#number-text").on('keyup', function (e) {
  if (e.keyCode == 13) {
    $('#btn-search-num').click();
  }
});

// Search number button [event]
$('#btn-search-num').click(function(e){
  var data = {
        'number': $("#number-text").val(),
        'rules': get_cookie_rules(),  // Should be already valid
      };

    // Check if the input contains only numbers
    if (!(/^\d+$/.test(data['number']))){
      alert("El valor introducido debe contener sólo números");
      return false;
    }

    // Change status text (feedback)
    $("#response-status").text("Última conexión: conectando...");

    // Send request
    $.ajax({
      url: "https://dev.aponti.es/ajax/get-number/",
      type: "POST",
      data: data,
      success: function (resp) {
        if (!resp["error"]) {
                    // Set received message
                    $("#response-text").text(resp["message"]);
                  } else {
                   $("#response-text").text("Se ha producido un error:\n" + resp["message"]);
                 }

                 // Set reception time
                var now = moment().format('LTS');
                $("#response-status").text("Última conexión: " + now);
               }
             }).fail(function (jqXHR, textStatus, error) {
                 $("#response-status").text("Última conexión: fallida");
            // Handle error here
            alert('THERE WAS AN ERROR DURING THE REQUEST!\n\nMore: \n\t' + textStatus + '\n\t' + error);
          });

});