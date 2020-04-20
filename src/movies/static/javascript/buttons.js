$("#submit").click(function(e) {
  e.preventDefault();
    location.href = '/'+ $('#movieTitle').val();
});


var mem = '';
$("#movieTitle").on("change paste keyup", function() {
  if($(this).val().length >= 3 && mem != $(this).val()){
    $.ajax({
      type: "POST",
      url: "/",
      data: {
        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
        'movieTitle': $('#movieTitle').val(),
        'requestType' : 0, // 0 stands for post actual text in searchbar
      },
      success: function (response) {
        console.log(response);
      }
    });
  }
  mem = $('#movieTitle').val();
});
