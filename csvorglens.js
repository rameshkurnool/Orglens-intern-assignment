const fs = require('fs');

// Read CSV file
const data = fs.readFileSync('orglensdata.csv', 'utf-8');

// Split into rows
const rows = data.trim().split('\n');

// Initialize variables
let sum = 0;
let sumSquared = 0;
let count = 0;
let values = [];

// Iterate over rows
for (let i = 0; i < rows.length; i++) {
  const columns = rows[i].split(',');
  const name = columns[0];
  const mark = parseInt(columns[1]);

  // Update variables
  sum += mark;
  sumSquared += mark * mark;
  count++;
  values.push(mark);
}

// Calculate mean, variance, and standard deviation
const mean = sum / count;
const variance = sumSquared / count - mean * mean;
const stdDev = Math.sqrt(variance);

// Write results to CSV file
const output = `Mean,${mean}\nVariance,${variance}\nStandard Deviation,${stdDev}`;
fs.writeFileSync('results.csv', output);

// Plot graph with mean and std dev markers
const plotly = require('plotly')('rameshkurnool20', '••••••••••');

const trace = {
    x: values,
    type: 'histogram',
    autobinx: false,
    xbins: {
      start: Math.min(...values),
      end: Math.max(...values),
      size: (Math.max(...values) - Math.min(...values)) / 10
    }
  };
const meanMarker = {
  type: 'line',
  x0: mean,
  x1: mean,
  y0: 0,
  y1: Math.max(...trace.y),
  line: {
    color: 'red',
    width: 2,
    dash: 'dot'
  }
};
const stdDevMarker1 = {
  type: 'line',
  x0: mean - stdDev,
  x1: mean - stdDev,
  y0: 0,
  y1: Math.max(...trace.y),
  line: {
    color: 'green',
    width: 2,
    dash: 'dot'
  }
};
const stdDevMarker2 = {
  type: 'line',
  x0: mean + stdDev,
  x1: mean + stdDev,
  y0: 0,
  y1: Math.max(...trace.y),
  line: {
    color: 'green',
    width: 2,
    dash: 'dot'
  }
};
const layout = {
  title: 'Distribution of Marks',
  xaxis: {
    title: 'Marks'
  },
  yaxis: {
    title: 'Count'
  },
  shapes: [meanMarker, stdDevMarker1, stdDevMarker2]
};
const graphOptions = { layout: layout, filename: 'marks-histogram', fileopt: 'overwrite' };
plotly.plot(trace, graphOptions, function (err, msg) {
  console.log(msg);
});
