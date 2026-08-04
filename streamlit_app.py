"""
Streamlit Dashboard - HR Executive Job-Hunt Copilot
====================================================
Giao diện web chuyên nghiệp chạy trên Streamlit.
Tự động mở trình duyệt mặc định khi chạy.
"""
import os
import sys
import time
import json
from pathlib import Path

import streamlit as st

# ========== Robust Imports for Streamlit Cloud (Linux) ==========
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
core_dir = os.path.join(current_dir, "core")
if core_dir not in sys.path:
    sys.path.insert(0, core_dir)

try:
    from core.cv_parser import CVParser
    from core.ai_engine import AIEngine
    from core.job_scraper import JobScraper
except ImportError:
    from cv_parser import CVParser
    from ai_engine import AIEngine
    from job_scraper import JobScraper

# ========== Page Config ==========
st.set_page_config(
    page_title="HR Job-Hunt Copilot | Nguyễn Văn Duy",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== Custom CSS ==========
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    .stApp {
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #0d9488 100%);
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        color: white;
    }

    .main-header h1 {
        font-size: 1.6rem;
        font-weight: 800;
        margin: 0;
        color: white;
    }

    .main-header p {
        font-size: 0.9rem;
        opacity: 0.85;
        margin: 4px 0 0 0;
    }

    .job-card {
        background: #1e293b;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
        color: #f1f5f9;
        transition: border-color 0.2s;
    }

    .job-card:hover {
        border-color: rgba(59,130,246,0.4);
    }

    .job-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 4px;
    }

    .company-name {
        font-size: 0.9rem;
        color: #06b6d4;
        font-weight: 600;
    }

    .match-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.2);
        color: #34d399;
        border: 1px solid rgba(16,185,129,0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
    }

    .tag {
        display: inline-block;
        background: rgba(59,130,246,0.15);
        color: #93c5fd;
        border: 1px solid rgba(59,130,246,0.25);
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        margin-right: 4px;
        margin-bottom: 4px;
    }

    .profile-section {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 14px;
        padding: 1.5rem;
        color: #e2e8f0;
    }

    .stat-box {
        text-align: center;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 1rem;
    }

    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #3b82f6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)


# ========== Initialize Services ==========
@st.cache_resource
def load_services():
    parser = CVParser()
    ai = AIEngine()
    scraper = JobScraper()
    return parser, ai, scraper


parser, ai_engine, scraper = load_services()
profile = parser.get_candidate_profile()


# ========== Session State ==========
if "jobs" not in st.session_state:
    st.session_state.jobs = scraper.get_sample_jobs()

if "applied_jobs" not in st.session_state:
    st.session_state.applied_jobs = set()


# ========== Header ==========
st.markdown("""
<div class="main-header">
    <h1>🎯 HR Executive Job-Hunt Copilot</h1>
    <p>Hệ thống AI tự động tìm kiếm & nộp hồ sơ cho Nguyễn Văn Duy | Trưởng Phòng Hành Chính Nhân Sự</p>
</div>
""", unsafe_allow_html=True)


# ========== Sidebar: Profile ==========
with st.sidebar:
    st.markdown("### 👤 Hồ Sơ Ứng Viên")

    st.markdown(f"**{profile['name']}**")
    st.caption(profile['title'])

    st.markdown("---")

    st.markdown("📱 " + profile["contact"]["phone"])
    st.markdown("📧 " + profile["contact"]["email"])
    st.markdown("📍 " + profile["contact"]["location"])
    st.markdown("🔗 " + profile["contact"]["linkedin"])

    st.markdown("---")

    st.markdown("#### 🏅 Năng Lực Cốt Lõi")
    for skill in profile["skills"][:5]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("#### 🎓 Bằng Cấp & Chứng Chỉ")
    for edu in profile["education"][:3]:
        st.caption(f"• {edu}")

    st.markdown("---")

    # LinkedIn Sync Button
    st.markdown("#### 🔗 Đồng Bộ LinkedIn")
    if st.button("📋 Copy Headline cho LinkedIn", use_container_width=True):
        st.code(profile["headline"], language=None)
        st.success("Anh copy đoạn text trên và paste vào mục Headline trên LinkedIn!")

    if st.button("📋 Copy About cho LinkedIn", use_container_width=True):
        st.code(profile["summary"], language=None)
        st.success("Anh copy đoạn text trên và paste vào mục About trên LinkedIn!")

    st.info("💡 Để mở trình duyệt tự động cập nhật LinkedIn, anh double-click file **DONG_BO_LINKEDIN.bat** trong thư mục dự án.")


# ========== Main Content: Stats Row ==========
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{len(st.session_state.jobs)}</div>
        <div>Việc Làm Tìm Thấy</div>
    </div>""", unsafe_allow_html=True)

with col2:
    high_match = len([j for j in st.session_state.jobs if j["match_score"] >= 80])
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{high_match}</div>
        <div>Match Score ≥ 80%</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{len(st.session_state.applied_jobs)}</div>
        <div>Đã Nộp Hồ Sơ</div>
    </div>""", unsafe_allow_html=True)

with col4:
    avg_score = sum(j["match_score"] for j in st.session_state.jobs) // max(len(st.session_state.jobs), 1)
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{avg_score}%</div>
        <div>Điểm TB Phù Hợp</div>
    </div>""", unsafe_allow_html=True)

st.markdown("---")


# ========== Job Listings ==========
st.markdown("### 🔥 Danh Sách Việc Làm Được AI Chọn Lọc & Chấm Điểm")

for idx, job in enumerate(st.session_state.jobs):
    is_applied = job["id"] in st.session_state.applied_jobs

    with st.container():
        top_col1, top_col2 = st.columns([4, 1])

        with top_col1:
            st.markdown(f"#### {job['title']}")
            st.markdown(f"🏢 **{job['company']}**")

        with top_col2:
            color = "#34d399" if job["match_score"] >= 80 else ("#fbbf24" if job["match_score"] >= 70 else "#94a3b8")
            st.markdown(f"<div style='text-align:center;'><span style='font-size:1.8rem;font-weight:800;color:{color};'>{job['match_score']}%</span><br><small>Match Score</small></div>", unsafe_allow_html=True)

        meta_col1, meta_col2, meta_col3 = st.columns(3)
        with meta_col1:
            st.caption(f"💰 {job['salary']}")
        with meta_col2:
            st.caption(f"📍 {job['location']}")
        with meta_col3:
            st.caption(f"🌐 {job['source']} • {job['posted_date']}")

        st.caption(job["description"][:200] + "...")

        # Keywords
        if job.get("matching_keywords"):
            kw_html = " ".join([f"<span class='tag'>{kw}</span>" for kw in job["matching_keywords"]])
            st.markdown(kw_html, unsafe_allow_html=True)

        # Action buttons
        btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 2])

        with btn_col1:
            if is_applied:
                st.success("✅ Đã Nộp Hồ Sơ")
            else:
                if st.button(f"🚀 1-Click Nộp Đơn", key=f"apply_{job['id']}"):
                    st.session_state.applied_jobs.add(job["id"])
                    st.success(f"Đã nộp hồ sơ thành công cho {job['company']}!")
                    st.rerun()

        with btn_col2:
            if st.button(f"📝 Xem Cover Letter", key=f"cl_{job['id']}"):
                st.session_state[f"show_cl_{job['id']}"] = not st.session_state.get(f"show_cl_{job['id']}", False)

        # Show Cover Letter if toggled
        if st.session_state.get(f"show_cl_{job['id']}", False):
            with st.expander(f"Cover Letter - {job['company']}", expanded=True):
                edited_letter = st.text_area(
                    "Chỉnh sửa Cover Letter trước khi nộp:",
                    value=job["cover_letter"],
                    height=300,
                    key=f"letter_{job['id']}"
                )
                if st.button(f"💾 Lưu & Nộp với Cover Letter này", key=f"save_cl_{job['id']}"):
                    job["cover_letter"] = edited_letter
                    st.session_state.applied_jobs.add(job["id"])
                    st.success("Đã lưu Cover Letter và nộp hồ sơ thành công!")
                    st.rerun()

        st.markdown("---")


# ========== Footer ==========
st.markdown("---")
st.caption("HR Executive Job-Hunt Copilot © 2026 | AI-Powered by Gemini & Antigravity | Dành cho Nguyễn Văn Duy")
