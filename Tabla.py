import webbrowser
pagina = """
<html>
<head>
<title></title>
<style>
    body{
        background-color:black;
        font-size:100%;
        font-family:Time New Roman;
    }
    #tab{
        width:60%;
        background-color:black;
        border:3px solid white;
        color:white;
        border-radius:10px;
        font-family: "Times New Roman";
        text-align:center;
    }
    h1{
        text-align:center;
        font-family: "Times New Roman";
        color:white;
    }
    .celda{
        background-color:rgb(20,20,20);
        text-align:center;
        font-family: "Times New Roman";
        padding:5px 10px;
        border:1px solid white;
        border-radius:3px;
    }
    footer{
        position:fixed;
        top:96%;
        left:1%;
        color:white;
        font-size:90%;
        font-family: "Times New Roman";

    }
</style>
</head>
<body><br><h1>Reporte de 10 datos</h1><br>
<center>
    <table id="tab">
        <tr>
            <td>No.</td><td>Nombre</td><td>Edad</td><td>Activo</td><td>Saldo</td>
        </tr><tr>
            <td>1</td><td>Carlos</td><td>28</td><td>Verdadero</td><td>40</td>
        </tr><tr>
            <td>2</td><td>Armando</td><td>25</td><td>Falso</td><td>45</td>
        </tr><tr>
            <td>3</td><td>Renato</td><td>30</td><td>Falso</td><td>50</td>
        </tr><tr>
            <td>4</td><td>Rodrigo</td><td>14</td><td>Verdadero</td><td>41</td>
        </tr><tr>
            <td>5</td><td>Pablo</td><td>19</td><td>Falso</td><td>20</td>
        </tr><tr>
            <td>6</td><td>María</td><td>54</td><td>Verdadero</td><td>42</td>
        </tr><tr>
            <td>7</td><td>Gerardo</td><td>22</td><td>Verdadero</td><td>34</td>
        </tr><tr>
            <td>8</td><td>Roberto</td><td>58</td><td>Falso</td><td>16</td>
        </tr><tr>
            <td>9</td><td>Mario</td><td>39</td><td>Verdadero</td><td>12</td>
        </tr><tr>
            <td>10</td><td>Bartolomé</td><td>33</td><td>Falso</td><td>32</td>
        </tr>
    </table><br><br><br>
</center>
<footer>Todos los derechos reservados por Romeo Ernesto Marroquín Sánchez (Meoer8Marsan)</footer>
</body>
</html>"""
reporte = open('Tabla.html', 'w')
reporte.write(pagina)
reporte.close()
webbrowser.open_new_tab('Tabla.html')