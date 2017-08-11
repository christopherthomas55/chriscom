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

function checkSmallerTen(value){
    if(value<10){
        value="0"+value;
    }
    return value;
}
function clockIncrement(array,element){
    sec=array[3]+1;
    min=array[2]+Math.floor(sec/60);
    hr=array[1]+ Math.floor(min/60);
    day=array[0]+Math.floor(hr/24);
    sec=sec%60;
    min=min%60;
    hr=hr%60;
    $(element).html(day+':'+checkSmallerTen(hr)+':'+checkSmallerTen(min)+':'+checkSmallerTen(sec));
    return [day, hr, min, sec]
}
function clock(element){
    var now = new Date();
    var h = now.getHours();
    var m = now.getMinutes();
    var s = now.getSeconds();
    h=checkSmallerTen(h);
    m=checkSmallerTen(m);
    s=checkSmallerTen(s);
    var monthArray = ['Jan', 'Feb', 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var dayArray = ['Sun', 'Mon', 'Tue', 'Wed','Thu', 'Fri', 'Sat'];
    var day = dayArray[now.getDay()];
    var month = monthArray[now.getMonth()];
    var year = now.getFullYear();

    $(element).html(h+':'+m+':'+s+' '+day+' '+month+' '+year)
}

$(document).ready(function() {
    randomize_color('.data-random')
});

window.setInterval(function(){
    clock('#clock');
},500);

