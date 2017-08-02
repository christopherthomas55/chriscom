/**
 * Created by chris_000 on 7/31/2017.
 */
function randomize_color(element){
    $(element).each(function(){
    var R = Math.floor(Math.random()*256);
    var G = Math.floor(Math.random()*256);
    var B = Math.floor(Math.random()*256);
    var trans = Math.random();
    $(this).css("background-color", 'rgba('+R+','+G+','+B+','+trans+')');
});}


$(document).ready(function() {
    randomize_color('.data-random')
});