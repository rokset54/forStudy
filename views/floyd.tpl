% rebase('layout.tpl', title=title, length=length, year=year, graph=graph, answer=answer)

<head>
	<link rel = "shortcut icon" href="https://atom.io/favicon.ico"/>
    <h2>Floyds algorithm</h2>
</head>
<style>

</style>
<body>

	<br>
	<br>
	<p style="font-size: 19px">
	The Floyd-Warshall algorithm is a popular algorithm for finding the shortest 
    path for each vertex pair in a weighted directed graph. In all pair shortest 
    path problem, we need to find out all the shortest paths from each vertex to 
    all other vertices in the graph. We’re taking a directed weighted graph
    G(V, E) as an input. And first, we construct a graph matrix from the given
    graph. This matrix includes the edge weights in the graph. Next, we insert
    in the diagonal positions in the matrix. The rest of the
    positions are filled with the respective edge weights from the input graph. 
    Then, we need to find the distance between two vertices. While finding the
    distance, we also check if there’s any intermediate vertex between two 
    picked vertices. If there exists an intermediate vertex then we check the 
    distance between the selected pair of vertices which goes through this
    intermediate vertex. If this distance when traversing through the
    intermediate vertex is less then the distance between two picked vertices
    without going through the intermediate vertex, we update the shortest distance 
    value in the matrix. The number of iterations is equal to the cardinality of 
    the vertex set. The algorithm returns the shortest distance from each vertex 
    to another in the given graph.
    </p>

    <div class="filter">
        <h3 class="title">Select the number of vertices (Min - 3, maximum - 10)</h3>
        <form method="post">
            <input type="number" value="{{length}}" min="3" max="10" name="CHANGE" />
            <input class="btn btn-primary" type="submit" name="BTN" value="Enter" />
        </form>
    </div>
	<div class="table">
        <form method="post">
            <table align="left" width="279" hspace="6" cellpadding="7" cellspacing="0" data-comment-id="40">
                <tbody>
                    %for idx1,element in enumerate(graph):
                    <tr valign="top">
                        %for idx2,current in enumerate(element):
                        <td width="18">
                            <input type="number" value="{{current}}" min="0" max="100" name="{{idx1}}{{idx2}}" />
                        </td>
                        %end
                    </tr>
                    %end
                </tbody>
            </table>
            <input class="invinsible-input" type="number" value="{{length}}" name="LENGTH" />
            <input class="btn btn-primary" type="submit" name="BTN" value="Calculate" />
        </form>
    </div>
    %if answer == "There is no decision":
    <h2 class="answer" style="color: tomato">{{answer}}</h2>
    %else:
    <h2 class="answer" style="color: green">{{answer}}</h2>


	<br>
	<br>
	

</body>

<address>
	<br>
	<br>
    <strong>Support:</strong>   <a href="mailto:sagas54@mail.ru">sagas54@mail.ru</a><br />
</address>
