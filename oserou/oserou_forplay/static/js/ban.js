/*
0 = blank
1 = black
2 = white 
*/

function buttonClick(e){
  refreshBoard(board_state);
  selected_row = this.row;
  selected_collumn = this.collumn;
  document.getElementById("board_state_send").value = board_state;
  document.getElementById("selected_row_send").value = selected_row;
  document.getElementById("selected_collumn_send").value = selected_collumn;
  document.getElementById("color_send").value = turn % 2 + 1;
  stoneColorChange(selected_row, selected_collumn, "red");
}

function stoneColorChange(row, collumn, new_color){
  let stone = document.getElementById("stone" + row + collumn);
  stone.style.backgroundColor = new_color;
}

function refreshBoard(board_state){
  for(let r = 0; r < 8; r++) {
    for(let c = 0; c < 8; c++) {
      let dic = ["gray", "black", "white"];
      let new_color = dic[board_state[r][c]];
      stoneColorChange(r, c, new_color);
    }
  }
}

function initBoard(){
  turn = 0;
  for(let i = 0; i < 8; i++) {
      if (i == 3){
        board_state[i] = [0, 0, 0, 2, 1, 0, 0, 0];
      }
      else if(i == 4){
        board_state[i] = [0, 0, 0, 1, 2, 0, 0, 0];
      }
      else{
        board_state[i] = new Array(8).fill(0);
      }
    }
  refreshBoard(board_state);
  alert("init!")
}

function init(){
  alert("init now");
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
  initBoard();
}
