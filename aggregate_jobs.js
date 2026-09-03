const fs = require('fs');
const path = require('path');

const resultsDir = './search_results';
const files = fs.readdirSync(resultsDir);

let allJobs = [];

files.forEach(file => {
  const filePath = path.join(resultsDir, file);
  const portal = file.startsWith('freehire') ? 'freehire-search' : 'linkedin-search';

  try {
    const content = fs.readFileSync(filePath, 'utf8');
    if (!content.trim()) return;

    const data = JSON.parse(content);
    const jobs = Array.isArray(data) ? data : (data.results || data.jobs || []);

    jobs.forEach(job => {
      allJobs.push({ ...job, portal });
    });
  } catch (e) {
    console.error(`Error parsing ${file}: ${e.message}`);
  }
});

console.log(JSON.stringify(allJobs, null, 2));
