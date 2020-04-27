var availableTags = [];

function showDropDown() {
  if(availableTags != 0){
    var myList = document.getElementsByClassName("dropdown")[0];
    myList.innerHTML = '';
    availableTags = JSON.parse(availableTags);
    Object.entries(availableTags).forEach(([key, value]) => {
      var movieP = document.createElement('p');
      var movieA = document.createElement('a');
      document.getElementsByClassName('dropdown')[0].appendChild(movieA);
      movieA.appendChild(movieP);
      movieA.href = value["title"];
      movieA.alt = value["title"];
      movieP.innerHTML = value["title"];
       console.log(value["title"]);
    });
  }
}


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
        availableTags = response;
        showDropDown();
      }
    });
  }
  mem = $('#movieTitle').val();
});

$( "#movieTitle" ).focus(function(){
  showDropDown();
});

$(window).click(function() {
  if (!($("movieTitle").is(":focus"))) {
    var myList = document.getElementsByClassName("dropdown")[0];
    myList.innerHTML = '';
  }
});

$('#movieTitle').click(function(event){
    event.stopPropagation();
});

//document.getElementById("myList").appendChild(node);
