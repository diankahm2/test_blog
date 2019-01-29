$(document).ready(function(){
  $('input').focus(function(){
    $(this).css('background-color', 'orange');
  });
  $('input').blur(function(){
    $(this).css('background-color','lightblue');
  });
});
