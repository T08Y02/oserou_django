function init(){
  let board = document.getElementById("board");

  for(let r = 0; r < 8; r++) {
    let tr = document.createElement("tr");
    for(let d = 0; d < 8; d++) {
      let td = document.createElement("td");
      td.className = "cell";
      td.setAttribute("id", "cell"+ (7 - d) + r);
      let ts = document.createElement("td");
      ts.className = "stone";
      ts.setAttribute("id", "stone"+ (7 - d) + r);
      td.appendChild(ts);
      tr.appendChild(td);
    }
    board.appendChild(tr);
  }
}