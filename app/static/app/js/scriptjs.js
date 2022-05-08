$(document).ready(function() {
    
    $(".delete").click(function(e){
        // alert($("#delete").val());
        
        let text = "Press a button!\nEither OK or Cancel.";
        if (confirm(text) == true) {
          text = "You pressed OK!";
          
          return true
        } else {
          text = "You canceled!"
          return false
        }
        
    //     $.post("{% url 'customer-delete' customer.id %}",
    //     {
    //         id :"{{ id }}",
    //         csrfmiddlewaretoken: '{{ csrf_token }}'
    //     },
    //     function(data,status){
    //       alert("Data: " + data + "\nStatus: " + status);
    //     });
    //   });
        
    // $.ajax({
    //     method: "POST",
    //     url: "{% url 'customer-delete' customer.id %}",
    //     headers: {'X-CSRFToken': '{{ csrf_token }}'},
    //     contentType: "application/json",
    //     dataType: 'json',
    //     data: { id:"{{customer.id}}" }
    // })
    // .fail(function(message) {
    //     alert('error');
    // })
    // .done(function(data) {
    //     alert(data);
    // });
});
});