var b1 = document.getElementById("index");
var b2 = document.getElementById("collect");
var b4 = document.getElementById("profile");
var detial_box = document.getElementById("detail");
var d1 = document.getElementById("detail-box");
var b3 = document.getElementById("message");


apiready = function () {
    api.parseTapmode();
}
var tab = new auiTab({
    element: document.getElementById("footer")
}, function (ret) {
    console.log(ret);
    if (ret.index == 4) {
        b4.setAttribute("style", "display:block")
        b1.setAttribute("style", "display:None")
        b2.setAttribute("style", "display:None")
        b3.setAttribute("style", "display:None")

        d1.setAttribute("style", "display:None")
        getuserinfo()
    }
    if (ret.index == 3) {
        b4.setAttribute("style", "display:None")
        b1.setAttribute("style", "display:None")
        d1.setAttribute("style", "display:None")
        b3.setAttribute("style", "display:Block")

        b2.setAttribute("style", "display:None")

    }
    if (ret.index == 2) {
        b4.setAttribute("style", "display:None")
        b1.setAttribute("style", "display:None")
        d1.setAttribute("style", "display:None")
        b3.setAttribute("style", "display:None")

        b2.setAttribute("style", "display:Block")
        var url = "/test/get_collect"
        var request = new XMLHttpRequest()
        request.open("GET", url)
        request.send()
        request.onreadystatechange = function () {
            if (request.readyState == 4 && request.status == 200) {
                var rs = request.responseText

                story_list = JSON.parse(rs)
                console.log('collect:' + story_list.content)
                box = {items: story_list.content}
                var tmp = document.getElementById("collect_tmp").innerHTML
                output = Mustache.render(tmp, box);
                var list = document.getElementById("collect")
                list.innerHTML = output
            }
        }
    }
    if (ret.index == 1) {
        b1.setAttribute("style", "display:block")
        b4.setAttribute("style", "display:None")
        d1.setAttribute("style", "display:None")
        b2.setAttribute("style", "display:None")
        b3.setAttribute("style", "display:None")

    }
});


//获取首页展示
function get() {
    var url = "/data"
    var request = new XMLHttpRequest()
    request.open("GET", url)
    request.send()
    request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
            var rs = request.responseText

            story_list = JSON.parse(rs)

            box = {items: story_list}
            var tmp = document.getElementById("tmp").innerHTML
            output = Mustache.render(tmp, box);
            var list = document.getElementById("content")
            list.innerHTML = output
            get_item_by_similaruser()
        }
    }

    var douban = "/test/mv"
    var r2 = new XMLHttpRequest()
    r2.open("GET", douban)
    r2.send()
    r2.onreadystatechange = function () {
        if (r2.readyState == 4 && r2.status == 200) {
            var rs = r2.responseText

            var mv = JSON.parse(rs)
            mv.content['type'] = mv.type
            //mv.content['summary']=mv.content.summary.slice(0,30)
            var tmp = document.getElementById("mv-tmp").innerHTML
            output = Mustache.render(tmp, mv.content);
            var db = document.getElementById("douban-box")
            db.innerHTML = output
        }
    }


}

function getdetail(id) {
    var url = "/detail/" + id
    var request = new XMLHttpRequest()
    request.open("GET", url)
    request.send()
    request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
            var detail = request.responseText
            detail = JSON.parse(detail)
            b1.setAttribute("style", "display:None")
            b4.setAttribute("style", "display:None")
            b2.setAttribute("style", "display:None")
            d1.setAttribute("style", "display:Block")
            b3.setAttribute("style", "display:None")
            detial_box.innerHTML = detail.content
            d1.setAttribute("value", id)
        }
    }
}


//详情页返回
function d_back() {

    d1.setAttribute("style", "display:None")
    b1.setAttribute("style", "display:Block")

}

//收藏资源
function collect() {
    id = d1.getAttribute("value")
    var url = "/collect/" + id

    var request = new XMLHttpRequest()
    request.open("GET", url)
    request.send()
    request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
            console.log(request.responseText)
        }
    }
}


function getuserinfo() {
    var url = "/test/userinfo"
    var request = new XMLHttpRequest()
    request.open("GET", url)
    request.send()
    request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
            var user = JSON.parse(request.responseText)
            var userinfo = document.getElementById("userinfo").innerHTML
            output = Mustache.render(userinfo, user.message);
            var profile = document.getElementById("profile-show")
            profile.innerHTML = output
            getlabels()
        }
    }
}


function get_item_by_similaruser() {
    var
        url = '/similaruser'
    var request = new XMLHttpRequest()
    request.open("GET", url)
    request.send()
    request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
            rawdata = request.responseText
            rs = JSON.parse(rawdata)
            data = rs.data
            data['name'] = rs.similaruser.name
            if (rs.status == 1) {
                var smtmp = document.getElementById("sm_tmp").innerHTML
                output = Mustache.render(smtmp, data);
                var smhtml = document.getElementById("similaruser")
                smhtml.innerHTML = output


            }
            else {
                console.log("No similar item")
            }


        }
    }

}

function getlabels() {
    var temp = document.getElementById('labels').innerHTML
    var obj = document.getElementById('label-box')
    var url = '/labels'
    var request = new XMLHttpRequest()
    request.open("GET", url)
    request.send()
    request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
            var data = JSON.parse(request.responseText)
            msg = {'content': data}
            output = Mustache.render(temp, msg);
            obj.innerHTML = output

        }
    }

}