(function() {
    var width = 700,
        height = 700;

    var svg = d3.select("#chart1")
        .append("svg")
        .attr("height", height)
        .attr("width", width)
        .append("g")
        .attr("transform", "translate(" + width/2 + ","+ height/2+")")

        // select the svg area
    var mysvg = d3.select("#my_dataviz")
        .append("circle").attr("cx",400).attr("cy",130).attr("r", 6).style("fill", "#69b3a2")
        .append("circle").attr("cx",200).attr("cy",160).attr("r", 6).style("fill", "#404080")
        .append("text").attr("x", 220).attr("y", 130).text("variable A").style("font-size", "15px").attr("alignment-baseline","middle")
        .append("text").attr("x", 220).attr("y", 160).text("variable B").style("font-size", "15px").attr("alignment-baseline","middle")
    
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
    
    var toolTip = d3.select('body')
        .append('div')
        .attr("class", "tooltip")
        .attr('id', 'tooltip')
        .attr('style', 'position: absolute; opacity: 0;')
        .style("right", (d3.event.pageX + 10) + "px")
        .style("top", (d3.event.pageY - 20) + "px");

    function ready (error, datapoints) {
        var circles = svg.selectAll(".ticker")
            .data(datapoints)
            .enter().append("circle")
            .attr("class", "ticker")
            .attr("r", function(d) {
                return radiusScale(d.score)
            })
            .attr("fill", function(d) {
                if (d.Industry == 'Consumer Cyclical') {return "darkblue"}
                if (d.Industry == 'Communication Services') {return "lightblue"}
                if (d.Industry == 'Technology') {return "lightgreen"}
                if (d.Industry == 'Healthcare') {return "red"}
                if (d.Industry == 'Energy') {return "darkgreen"}
                if (d.Industry == 'Financial Services') {return "pink"}
                if (d.Industry == 'Basic Materials') {return "gray"}
                if (d.Industry == 'Industrials') {return "black"}
            })
            .on('mouseover', function (d) {
                d3.select('#tooltip')
                    .transition()
                    .duration(200)
                    .style('opacity', 1)

                d3.select('#tooltip').html(d.company + " ("+ d.ticker + ")" + "<br>" + "Industry: " + d.Industry + "<br/>" + "Score: " + d.score + "<br/>" + "2021 Performance: " + d.performance + "%")
                    .style("left", (d3.event.pageX + 10) + "px")
                    .style("top", (d3.event.pageY + 10) + "px");
            })
            .on('mouseout', function () {
                d3.select('#tooltip').style('opacity', 0)
            })
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

        circles.append("text")
            .text(function(d) {return d.ticker})
    
    }
})();
