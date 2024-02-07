//-------------------------------------------------------------------------------------------------
// function to change the dropdown menu from index.html / handle the events
//-------------------------------------------------------------------------------------------------
function optionChanged(selectedOption) {
    if (selectedOption === "option1") {
      d3.select("#data-cleaning-container").style("display", "block");
      d3.select("ml-container").style("display", "none");
      
    } else if (selectedOption === "option2") {
      d3.select("#data-cleaning-container").style("display", "none");
      d3.select("#ml-container").style("display", "block");
      
    } 
  }