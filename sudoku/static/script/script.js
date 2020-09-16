var line = "012345678".split("")
var column = "012345678".split("")

function clearSudoku() {
    for (l = 0; l < 9; l++) {
        for (c = 0; c < 9; c++) {
            document.getElementById(line[l] + column[c]).values = "";
        }
    }
}