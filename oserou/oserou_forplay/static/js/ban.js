/*
0 = blank
1 = black
2 = white 
*/

function buttonClick(e){
  alert('Click' + this.row +  this.collumn);
  refreshBoard();
}

function stoneColorChange(row, collumn, new_color){
  let stone = document.getElementById("stone" + row + collumn);
  stone.style.backgroundColor = new_color;
}

function refreshBoard(boardState){

  for(let r = 0; r < 8; r++) {
    for(let c = 0; c < 8; c++) {
      let dic = ["gray", "black", "white"];
      let new_color = dic[boardState[r][c]];
      stoneColorChange(r, c, new_color);
    }
  }
}

function init(){
  let board = document.getElementById("board");
  for(let r = 0; r < 8; r++) {
    let tr = document.createElement("tr");
    for(let c = 0; c < 8; c++) {
      let td = document.createElement("td");
      td.className = "cell";
      td.setAttribute("id", "cell"+ r + c);
      let ts = document.createElement("td");
      ts.className = "stone";
      ts.setAttribute("id", "stone"+ r + c);
      ts.addEventListener('click', {row:r, collumn:c, handleEvent:buttonClick});
      td.appendChild(ts);
      tr.appendChild(td);
    }
    board.appendChild(tr);
  }

  //init board
  let boardState = new Array(8);
  for(let i = 0; i < 8; i++) {
      if (i == 3){
        boardState[i] = [0, 0, 0, 2, 1, 0, 0, 0];
      }
      else if(i == 4){
        boardState[i] = [0, 0, 0, 1, 2, 0, 0, 0];
      }
      else{
        boardState[i] = new Array(8).fill(0);
      }
    }
    alert(boardState);
    refreshBoard(boardState);
}
