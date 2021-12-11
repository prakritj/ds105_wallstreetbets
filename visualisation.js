(function() {
    var width = 500,
        height = 500;

    var svg = d3.select("#chart")
        .append("svg")
        .attr("height", height)
        .attr("width", width)
        .append("g")
        .attr("transform", "translate(" + width/2 + ","+ height/2+")")
    
    var radiusScale = d3.scaleSqrt().domain([4981,360351]).range([10,80])

    var simulation = d3.forceSimulation()
        .force("x", d3.forceX().strength(0.05))
        .force ("y", d3.forceY().strength(0.05))
        .force("collide", d3.forceCollide(function(d) {
            return radiusScale(d.score) + 2
        }))
    d3.queue()
        .defer(d3.csv, "final_dataset.csv")
        .await(ready)
    
    function ready (error, datapoints) {

        var circles = svg.selectAll(".ticker")
            .data(datapoints)
            .enter().append("circle")
            .attr("class", "ticker")
            .attr("r", function(d) {
                return radiusScale(d.score)
            })
            .attr("fill", "lightblue")
        
        simulation.nodes(datapoints)
            .on('tick', ticked)
        
        function ticked() {
            circles
                .attr("cx", function(d) {
                    return d.x
                })
                .attr("cy", function(d) {
                    return d.y
                })
        }
    
    }
})();