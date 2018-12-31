function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {

  // if (ev.target.childNodes.length > 0){
  if (ev.target.hasChildNodes()){  
    alert("plage déjà enregistrée");
  }
  else
  {
     ev.preventDefault();
     var data = ev.dataTransfer.getData("text");
     var nodeCopy = document.getElementById(data).cloneNode(true);
     nodeCopy.id = "newId"; /* We cannot use the same ID */
     nodeCopy.setAttribute('draggable', false);
     ev.target.appendChild(nodeCopy);
     var idDraged = ev.dataTransfer.getData("text");
     var idHost = ev.target.id;
     TransferToServerrr(idDraged,idHost);
  }      

}


function TransferToServer(ed,eb){
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/saveTask');
      xhr.onload = function(){
        var data = this.responseText;
        //console.log(data);
      }

      var params =ed+"@"+eb;//cancatenation
      alert(params);
      xhr.send(params);
}

function TransferToServerrr(ed,eb){
$.ajax({
  type:'POST',
  url:'/saveTask',
  data:{
    idProject:ed,
    idPlage:eb
  },
  success:function(){
    // alert("created success");

  }
});
}

function TransferToServer2(ed){
$.ajax({
  type:'POST',
  url:'/deleteTask',
  data:{
    idPlage:ed
  },
  success:function(){
    // alert("created success");

  }
});
}




function putProjectIntoPlage(idPlage, idProject){
  var nodeHost = document.getElementById(idPlage);
  var nodeCopy = document.getElementById(idProject).cloneNode(true);
  nodeCopy.id = "newId";
  nodeCopy.setAttribute('draggable', false);
  nodeHost.appendChild(nodeCopy);
}

function deleteTask(ev,id){
  ev.preventDefault();
  var node = document.getElementById(id);
  if (node.hasChildNodes()){
    if (confirm('delete this task ?')){
      node.removeChild(node.firstChild);
      TransferToServer2(id);
    }
  }
}

function hexColor()
{
  var hue = 'rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ')';

  return hue;
}

function previous()
{
  alert();
$.ajax({
  type:'POST',
  url:'/previous',
}); 
}

function next()
{
  alert();
$.ajax({
  type:'POST',
  url:'/next',
}); 
}