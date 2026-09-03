const fs = require('fs');
const path = require('path');

const inputFile = path.join(__dirname, 'all_job_results.json');
const outputFile = path.join(__dirname, 'top_20_jobs.json');

try {
    const data = JSON.parse(fs.readFileSync(inputFile, 'utf8'));

    // Filter for high-relevance keywords and remove duplicates
    const keywords = [
        'generative', 'llm', 'rag', 'ai engineer', 'data engineer',
        'databricks', 'pyspark', 'ml engineer', 'pytorch', 'tensor flow'
    ];

    const scoredJobs = data.map(job => {
        let score = 0;
        const text = `${job.title} ${job.company} ${job.description || ''}`.toLowerCase();

        keywords.forEach(kw => {
            if (text.includes(kw)) score += 1;
        });

        return { ...job, relevance_score: score };
    });

    const top20 = scoredJobs
        .sort((a, b) => b.relevance_score - a.relevance_score)
        .slice(0, 20);

    fs.writeFileSync(outputFile, JSON.stringify(top20, null, 2));
    console.log(`Curated top 20 jobs into ${outputFile}`);
} catch (err) {
    console.error('Error curating jobs:', err);
    process.exit(1);
}
