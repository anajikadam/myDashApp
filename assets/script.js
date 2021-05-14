// window.setTimeout(function () {
//   alert("hello");
//   window.location.reload();
// }, 30000);



function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
  }
  
  function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
  }


  $(function(){
    $('#pg1').on('click', function(){
       alert('click event');
    });
});
 
  $(".nav-link").click(function () {
    $(".nav-link").removeClass("active");
    $(this).addClass("nav-link active");   
});



