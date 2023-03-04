/*
0 = blank
1 = black
2 = white 
*/

function buttonClick(e){
  alert('Click' + this.row +  this.collumn);
  alert(e.target.style.background-color)
  //stoneColorChange("black")
}

function stoneColorChange(e){
  let stone = e.target;
  stone.style.color = new_color;
}

function init(){
  let board = document.getElementById("board");

  for(let r = 0; r < 8; r++) {
    let tr = document.createElement("tr");
    for(let d = 0; d < 8; d++) {
      let td = document.createElement("td");
      td.className = "cell";
      td.setAttribute("id", "cell"+ d + r);
      let ts = document.createElement("td");
      ts.className = "stone";
      ts.setAttribute("id", "stone"+ d + r);
      ts.addEventListener('click', {collumn:d, row:r, handleEvent:buttonClick});
      td.appendChild(ts);
      tr.appendChild(td);
    }
    board.appendChild(tr);
  }
}
