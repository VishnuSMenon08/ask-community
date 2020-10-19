function expandComments(answer_id){
    document.getElementById("comment"+answer_id).className = "display clear";
}

function closeQuery(){

    document.getElementById("ask-tab").className = "ask hidden";
}

function openQuery(){
    document.getElementById("ask-tab").className = "display ask";
}