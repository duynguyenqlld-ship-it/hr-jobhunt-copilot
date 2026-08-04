import os
import json
from flask import Flask, render_template, jsonify, request
import config
from core.cv_parser import CVParser
from core.ai_engine import AIEngine
from core.job_scraper import JobScraper
from core.browser_automation import BrowserAutomation

app = Flask(__name__, template_folder="templates")

# Initialize core services
parser = CVParser()
ai_engine = AIEngine()
scraper = JobScraper()
automation = BrowserAutomation()

# In-memory storage for scanned jobs & application history
JOBS_STORE = scraper.get_sample_jobs()
APPLIED_HISTORY = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/profile", methods=["GET"])
def get_profile():
    profile = parser.get_candidate_profile()
    return jsonify({
        "status": "success",
        "profile": profile
    })

@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    return jsonify({
        "status": "success",
        "total": len(JOBS_STORE),
        "jobs": JOBS_STORE,
        "applied_count": len(APPLIED_HISTORY)
    })

@app.route("/api/apply", methods=["POST"])
def apply_job():
    data = request.json or {}
    job_id = data.get("job_id")
    custom_cover_letter = data.get("cover_letter")

    target_job = next((j for j in JOBS_STORE if j["id"] == job_id), None)
    if not target_job:
        return jsonify({"status": "error", "message": "Công việc không tồn tại!"}), 404

    cover_letter = custom_cover_letter or target_job["cover_letter"]
    
    # Run browser auto-apply
    res = automation.apply_to_job(
        job_id=target_job["id"],
        job_title=target_job["title"],
        company_name=target_job["company"],
        job_url=target_job["url"],
        cover_letter=cover_letter
    )

    # Update job state
    target_job["applied_status"] = "Đã nộp hồ sơ"
    target_job["applied_at"] = res["applied_at"]
    
    if target_job not in APPLIED_HISTORY:
        APPLIED_HISTORY.append(target_job)

    return jsonify({
        "status": "success",
        "result": res,
        "job": target_job,
        "applied_count": len(APPLIED_HISTORY)
    })

@app.route("/api/sync_linkedin", methods=["POST"])
def sync_linkedin():
    data = request.json or {}
    headline = data.get("headline")
    summary = data.get("summary")

    res = automation.sync_to_linkedin(headline=headline, summary=summary)
    return jsonify({
        "status": "success",
        "result": res
    })

@app.route("/api/check_linkedin", methods=["GET"])
def check_linkedin():
    profile = parser.get_candidate_profile()
    return jsonify({
        "status": "success",
        "linkedin_url": f"https://{profile['contact']['linkedin']}",
        "headline": profile["headline"],
        "summary": profile["summary"],
        "experiences": profile["experiences"]
    })

@app.route("/api/generate_cover_letter", methods=["POST"])
def generate_cover_letter():
    data = request.json or {}
    job_title = data.get("job_title", "Trưởng phòng HCNS")
    company_name = data.get("company_name", "Quý Công Ty")
    job_desc = data.get("job_description", "")

    letter = ai_engine.generate_cover_letter(job_title, company_name, job_desc)
    return jsonify({
        "status": "success",
        "cover_letter": letter
    })

if __name__ == "__main__":
    print("Starting HR Job-Hunt & LinkedIn Automation Web Dashboard...")
    print("Server running on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
