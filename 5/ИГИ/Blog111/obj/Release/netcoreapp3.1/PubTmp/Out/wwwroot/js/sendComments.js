"use strict";
var options = { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: true };




var connection = new signalR.HubConnectionBuilder().withUrl("/comments").build();
document.getElementById("send").disabled = true;

connection.start().then(AddToGroup);

connection.on("addComment", function (post, user, message) {
    console.log("asdasdasd");
    var d = new Date();
    
    var item = '<div class="comment-body"><h4 class="commenter-name">' + user + '</h4><div class="comment-date">' + d.toLocaleString('en-US', options).replace(",", "") +'</div><p class="comment-message">'+message+'</div><hr>';
    var li = document.createElement("li");
    li.innerHTML = item;
    document.getElementById("comlist").appendChild(li);
});
connection.start().then(function () {
    document.getElementById("send").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("send").addEventListener("click", function (event) {
    var uF = document.getElementById("uF").value;
    var uL = document.getElementById("uL").value;
    var post = document.getElementById("postId").value;
    var user = uF.concat(" ").concat(uL);
    var message = document.getElementById("content").value;
    
    connection.invoke("addComment", post, message).catch(function (err) {
        return console.error(err.toString());
    });
    event.preventDefault();
});
function AddToGroup() {
    document.getElementById("send").disabled = false;
    var postId = document.getElementById("postId").value;
    connection.invoke("AddToGroup", postId)
}
