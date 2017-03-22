var n = 0;

function doTable() {
    n = document.getElementById('n').value;
    var divtabla = document.getElementById('divtabla');
    divtabla.innerHTML = '';
    divtabla.innerHTML = '<table id="tabla"></table>';
    var tabla = document.getElementById('tabla');
    for (var i = 0; i < n; i++) {
        var row = tabla.insertRow(i);
        for (var j = 0; j < n; j++) {
            var cellinrow = row.insertCell(j);
            var fondo = '';
            var deshabilitado = '';
            if (i === j) {
                deshabilitado = 'disabled';
                fondo = 'style = "background-color: black; border-color: transparent;"';
            }
            cellinrow.innerHTML = '<input type="button" id="' + i + ',' + j + '" onclick="changevalue(\'' + i + ',' + j + '\')" value="0"' + deshabilitado + ' ' + fondo + '/>';
        }
        var lastcell = row.insertCell(n);
        lastcell.innerHTML = ' ' + i;
    }
    var lastrow = tabla.insertRow(n);
    for (var o = 0; o < n; o++) {
        var cellinrow1 = lastrow.insertCell(o);
        cellinrow1.innerHTML = '&nbsp;&nbsp;' + o;
    }

}

function reverse(s) {
    return s.split("").reverse().join("");
}

function changevalue(id) {
    var boton = document.getElementById(id);
    var boton2 = document.getElementById(reverse(id));
    if (boton.value == '0') {
        boton.value = '1';
        boton2.value = '1';
    } else {
        boton.value = '0';
        boton2.value = '0';
    }
}

function doGraph() {
    var combobox = document.getElementById("tipoMatriz");
    var tipoMatriz = combobox.options[combobox.selectedIndex].value;
    if (tipoMatriz == 'A') {
        GrafoA();
    } else if (tipoMatriz == 'I') {
        GrafoI();
    } else {
        alert('Seleccione un tipo de matriz');
    }
}

var aristasArray;
var nodosArray;


function GrafoA() {
    nodosArray = [];
    aristasArray = [];
    for (var i = 0; i < n; i++) {
        var valorboton1 = document.getElementById(i + ',' + i).value;
        if (valorboton1 == 1) {
            alert('La matriz no puede tener 1\'s en la diagonal principal');
        }
        nodosArray.push({
            id: i,
            label: 'Nodo ' + i
        });
        for (var j = i + 1; j < n; j++) {
            var valorboton = document.getElementById(i + ',' + j).value;
            // var valorbotonopuesto = document.getElementById(j + ',' + i).value;
            // if (valorboton == valorbotonopuesto) {
            //     if (valorboton == '1') {
            //         aristasArray.push({
            //             from: i,
            //             to: j
            //         });
            //     }
            // } else {
            //     alert('La matriz introducida no es valida');
            //     return 0;
            // }
            if (valorboton == '1') {
                aristasArray.push({
                    from: i,
                    to: j
                });
            }
        }
    }
    if (document.getElementById("mynetwork") !== null) {
        document.getElementById("mynetwork").remove();
    }
    var divGrafo = document.createElement("div");
    divGrafo.id = 'mynetwork';
    document.body.appendChild(divGrafo);
    // create an array with nodes
    var nodes = new vis.DataSet(nodosArray);

    // create an array with edges
    var edges = new vis.DataSet(aristasArray);
    // create a network
    var container = document.getElementById('mynetwork');
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {};

    var network = new vis.Network(container, data, options);
    cuentaCiclosTotales();
}

function GrafoI() {

}

var checkedNodes = [];
var nodosChecados = 0;
var ciclos = [];
var ciclosFinal = [];
var ciclosFinalFinal = [];
var nodosdesdeelcero = [];
var addnodos = true;


function unico(arr) {
    var result = arr.filter(function(elem, pos) {
        return arr.indexOf(elem) == pos;
    });
    return result;
}

function cuentaCiclosTotales() {
    var esconexo = false;
    var aux = 0;
    var esprimeravuelta = true;
    var strconexo = '';
    nodosdesdeelcero = [];
    addnodos = true;
    aristasArray.forEach(function(arista) {

        checkedNodes = [];

        if (esprimeravuelta) {
            aux = parseInt(arista.from);
            nodosdesdeelcero.push(aux);
            esprimeravuelta = false;
        }

        if (arista.from !== aux) {
            addnodos = false;
            if (unico(nodosdesdeelcero).length == n) {
                esconexo = true;
            }
            nodosdesdeelcero = [];
        }

        cuentaCiclosPorNodo(arista.from, arista.from, arista.to);

    });

    if (esconexo) {
        strconexo = 'El grafo es conexo';
    } else {
        strconexo = 'El grafo no es conexo';
    }
    // cuentaCiclosPorNodo(aristasArray[0].from, aristasArray[0].from, aristasArray[0].to);
    // console.log('--------------------');
    checkedNodes = [];

    var ciclosoriginal = [];
    for (var i = 0; i < ciclos.length; i++) {
        ciclosoriginal.push(ciclos[i].slice());
        ciclos[i].sort();
    }
    // console.log('ciclosOriginal: ', ciclosoriginal);
    // console.log('ciclosFinal: ', ciclos);

    eliminaciclosduplicados(ciclos, ciclosoriginal);
    // console.log('uniq: ', ciclosFinal);
    // console.log('uniqFinal: ', ciclosFinalFinal);
    var divciclos = document.getElementById('ciclos');
    if (ciclosFinalFinal.length === 0) {
        divciclos.innerHTML = '<b>' + strconexo + '</b><br><u>Este grafo no tiene ciclos</u>';
    } else {
        var htmldivciclos = '<font size="4"><b>' + strconexo + '</b><br><u>Ciclos del grafo:</u><br><ul>';
        for (var l = 0; l < ciclosFinalFinal.length; l++) {
            htmldivciclos += '<li>' + ciclosFinalFinal[l] + '</li>';
        }
        htmldivciclos += '</ul></font>';
        divciclos.innerHTML = htmldivciclos;
    }

    checkedNodes = [];
    nodosChecados = 0;
    ciclos = [];
    ciclosFinal = [];
    ciclosFinalFinal = [];


}

function cuentaCiclosPorNodo(nodoAbuscar, nodoAnterior, nodoActual) {
    if (addnodos) {
        nodosdesdeelcero.push(nodoActual);
    }
    console.log('nodoActual: ', nodoActual);
    var flag = false;
    var conexionesdelnodoactual = AristasDelNodo(nodoActual, nodoAnterior);

    console.log('conexionesdelnodoactual: ', conexionesdelnodoactual);


    if (conexionesdelnodoactual.length === 0) {
        // console.log('no hay mas conexiones para el nodo: ' + nodoActual);
        flag = true;
    }

    if (yapasoporesenodo(nodoActual)) {
        // console.log('Ya se habia pasado por el nodo: ' + nodoActual);
        flag = true;
    }

    checkedNodes.push(nodoActual);
    nodosChecados += 1;
    // se compara que nodoschecados sea mayor a 2 por que se considera el nodo a buscar como un nodo a checar
    // es decir el nodoAbuscar tambien termina con estado de checado
    if (nodoActual === nodoAbuscar && nodosChecados > 2) {
        // console.log('Se encontro un ciclo para el nodo: ' + nodoAbuscar);
        // console.log('nodosChecados: ', checkedNodes);
        ciclos.push(checkedNodes.slice());
        // console.log('ciclos: ', ciclos);
        checkedNodes.pop();
        nodosChecados -= 1;
        return true;
    }

    if (flag) {
        checkedNodes.pop();
        nodosChecados -= 1;
        return false;
    }
    conexionesdelnodoactual.forEach(function(conexiondelnodoactual) {
        cuentaCiclosPorNodo(nodoAbuscar, nodoActual, conexiondelnodoactual);
    });

    checkedNodes.pop();
    nodosChecados -= 1;
    return false;
}

function AristasDelNodo(nodo, nodoaevitar) {
    var result = [];
    // console.log('nodoActual: ' + nodo);
    // console.log('nodoaevitar: ' + nodoaevitar);
    // console.log('checkedNodes: ', checkedNodes);
    aristasArray.forEach(function(arista) {
        if (arista.from === nodo && arista.to !== nodoaevitar && !yapasoporesenodo(arista.to)) {
            result.push(arista.to);
        } else if (arista.to === nodo && arista.from !== nodoaevitar && !yapasoporesenodo(arista.from)) {
            result.push(arista.from);
        }
    });
    return result;
}

function yapasoporesenodo(nodo) {
    for (var i = 0; i < checkedNodes.length; i++) {
        if (checkedNodes[i] == nodo) {
            // console.log('entro if');
            return true;
        }
    }
    return false;
}

function eliminaciclosduplicados(arrdeciclos, arrdeciclosoriginal) {
    for (var i = 0; i < arrdeciclos.length; i++) {
        if (noestaenciclosfinal(arrdeciclos[i])) {
            ciclosFinal.push(arrdeciclos[i]);
            ciclosFinalFinal.push(arrdeciclosoriginal[i]);
        }
    }
}

function noestaenciclosfinal(ciclo) {
    var flag = false;
    for (var i = 0; i < ciclosFinal.length; i++) {
        if (losarrsoniguales(ciclosFinal[i], ciclo)) {
            return false;
        }
    }
    return true;
}

function losarrsoniguales(arr1, arr2) {
    var flag = true;
    if (arr1.length == arr2.length) {
        for (var i = 0; i < arr1.length; i++) {
            if (arr1[i] !== arr2[i]) {
                flag = false;
            }
        }
    } else {
        flag = false;
    }

    return flag;

}
