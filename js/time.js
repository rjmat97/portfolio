function getTime(){
    var d = new Date();
    h = d.getHours();
    m = d.getMinutes();
    s = d.getSeconds();
    set = "AM"
    
    // console.log(d)
    if(h>12){
        h=h-12
        set="PM"
    }
    if(h/10<1) h = "0"+h
    if(m/10<1) m = "0"+m
    if(s/10<1) s = "0"+s
    time =h+":"+m + ":"+s + " "+set
    // console.log()
    document.getElementById("time").innerHTML = time
    imgrot(h,m)
    setTimeout(getTime, 1000);
}

function imgrot(h,m){
    var angleh = h*30
    var anglem = (m/5)*30
    var angles = (s/5)*30
    document.getElementById("morty").setAttribute("style", "transform: rotate(" + angleh + "deg)")
    document.getElementById("rick").setAttribute("style", "transform: rotate(" + anglem + "deg)")
    document.getElementById("portal").setAttribute("style", "transform: rotate(" + angles + "deg)")
}

