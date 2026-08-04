"""
Streamlit Dashboard - Executive Job-Hunt & COO Strategy Copilot
================================================================
Tích hợp vị trí COO (Giám Đốc Vận Hành) & HR Executive.
Thu thập việc làm từ JobsGO, Việc Làm 24h, Facebook HR Groups, TopCV, VietnamWorks.
"""
import os
import sys
import time
import json
import streamlit as st

# ========== Page Config ==========
st.set_page_config(
    page_title="Executive Job-Hunt & COO Copilot | Nguyễn Văn Duy",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== Expanded Profile (COO & HR Executive) ==========
PROFILE = {
    "name": "NGUYỄN VĂN DUY",
    "title": "COO (GIÁM ĐỐC VẬN HÀNH) | TRƯỞNG PHÒNG HÀNH CHÍNH NHÂN SỰ",
    "headline": "COO (Chief Operating Officer) | HRBP Strategic Partner | Tái Cấu Trúc Vận Hành & AI Digital HR",
    "contact": {
        "phone": "0902.741.792",
        "email": "duynguyen.qlld@gmail.com",
        "location": "Long Bình, Tp. Hồ Chí Minh",
        "linkedin": "linkedin.com/in/duynguyen-hr"
    },
    "summary": "Nhà Quản trị Vận hành & Nhân sự Cấp cao với 15 năm kinh nghiệm thực chiến điều hành hệ thống quy mô lớn (3.000+ nhân sự) đa lĩnh vực: FMCG, Sản xuất, Bán lẻ, Xây dựng & Bất động sản. Định hướng thử thách các vị trí COO (Chief Operating Officer) và CHRO/Head of HR. Nổi bật với tư duy tái cấu trúc chiến lược, tối ưu định biên 15%, thiết lập bản đồ chiến lược BSC/KPI chuẩn GSA nâng 18% năng suất lao động toàn doanh nghiệp. Tiên phong chuyển đổi số vận hành, ứng dụng thành thạo AI (Google Gemini, Antigravity 2.0 Agentic AI) cắt giảm 75% tác vụ thủ công.",
    "skills": [
        "COO Operations Management & Business Strategy",
        "Workforce Planning & Organizational Restructuring",
        "BSC / KPI / OKR Enterprise Performance Management",
        "Digital Transformation & AI Automation (Gemini, Antigravity 2.0)",
        "HRIS Systems (Base.vn, MISA AMIS, Lark People)",
        "Total Rewards & C&B System Design",
        "Labor Law, HSE & ISO 9001/16949 Compliance"
    ],
    "education": [
        "Cử nhân Quản trị Nguồn nhân lực — Đại học Lao động & Xã hội",
        "Chứng chỉ Giám đốc Điều hành (CEO) - DVL EDU (2019)",
        "Chứng chỉ Quản lý Dự án Chuyên nghiệp (Project Management) - Google (2024)",
        "Chứng chỉ Kỹ thuật xây dựng & triển khai BSC & KPI (2025)",
        "Đánh giá viên nội bộ ISO 9001:2015 & ISO/TS 16949"
    ]
}

# ========== Multi-Source Job Database (JobsGO, 24h, FB Groups, TopCV...) ==========
EXPANDED_JOBS = [
    {
        "id": "job_coo_001",
        "title": "Giám Đốc Vận Hành (COO - Chief Operating Officer) - Ngành FMCG & Bán Lẻ",
        "company": "Tập đoàn Sản Xuất & Chuỗi Bán Lẻ Thực Phẩm Đa Quốc Gia",
        "location": "Quận 1 / Quận 2, TP. Hồ Chí Minh",
        "salary": "60.000.000 - 85.000.000 VNĐ",
        "source": "JobsGO & Facebook Group (C-Level Vietnam)",
        "posted_date": "Vừa cập nhật",
        "match_score": 98,
        "matching_keywords": ["COO", "GIÁM ĐỐC VẬN HÀNH", "FMCG", "BÁN LẺ", "TÁI CẤU TRÚC", "BSC/KPI"],
        "description": "Điều hành toàn bộ chuỗi vận hành nhà máy sản xuất FMCG và 100+ cửa hàng bán lẻ. Tái cấu trúc sơ đồ tổ chức, cắt giảm 15-20% chi phí vận hành dư thừa. Chủ trì xây dựng bản đồ chiến lược BSC/KPI từ CEO xuống các khối, đẩy mạnh chuyển đổi số và ứng dụng AI tự động hóa vận hành.",
        "cover_letter": """Kính gửi Hội đồng Quản trị & Ban Giám đốc Tập đoàn Sản Xuất & Chuỗi Bán Lẻ Thực Phẩm,

Tôi là Nguyễn Văn Duy, chuyên gia 15 năm kinh nghiệm điều hành và tái cấu trúc hệ thống vận hành quy mô lớn (3.000+ nhân sự). Tôi rất hào hứng gửi hồ sơ ứng tuyển vị trí Giám Đốc Vận Hành (COO).

Với năng lực từng trực tiếp thiết kế lại sơ đồ tổ chức tinh gọn 15% định biên hành chính dư thừa, triển khai BSC & KPI chuẩn GSA nâng 18% năng suất toàn doanh nghiệp, cùng thế mạnh tiên phong ứng dụng AI (Google Gemini, Antigravity 2.0) cắt giảm 75% tác vụ thủ công, tôi tin tưởng sẽ giúp Quý Tập đoàn tối ưu chi phí vận hành và tăng trưởng doanh thu bền vững.

Trân trọng,
Nguyễn Văn Duy - COO / Executive HR Director
Điện thoại: 0902.741.792 | Email: duynguyen.qlld@gmail.com"""
    },
    {
        "id": "job_coo_002",
        "title": "Giám Đốc Vận Hành Khối Doanh Nghiệp (COO / Operation Director)",
        "company": "Tập đoàn Đầu Tư & Phát Triển Bất Động Sản Đô Thị",
        "location": "TP. Thủ Đức, TP. Hồ Chí Minh",
        "salary": "70.000.000 - 90.000.000 VNĐ",
        "source": "Facebook Group (Executive Headhunter Vietnam)",
        "posted_date": "Hôm nay",
        "match_score": 96,
        "matching_keywords": ["COO", "BẤT ĐỘNG SẢN", "CEO STRATEGY", "OKRS", "ĐỊNH BIÊN"],
        "description": "Sát cánh cùng Chủ tịch & CEO điều hành toàn bộ công tác vận hành khối dự án BĐS, Hành chính Nhân sự, Pháp lý và IT. Định biên nhân sự tối ưu, quản lý rủi ro pháp lý hợp đồng lao động và xây dựng văn hóa doanh nghiệp hiệu suất cao.",
        "cover_letter": """Kính gửi Chủ tịch & Hội đồng Quản trị Tập đoàn Bất Động Sản Đô Thị,

Tôi là Nguyễn Văn Duy, ứng viên vị trí Giám Đốc Vận Hành (COO). Tôi từng giữ chức vụ Trưởng phòng HCNS Công ty BĐS Nhật Tiến và có chứng chỉ Giám đốc Điều hành (CEO), Chứng chỉ Quản lý Dự án Google (PMP).

Năng lực lõi của tôi là hoạch định định biên chiến lược, số hóa quy trình vận hành và kiểm soát tuân thủ pháp lý 100%.

Rất mong được gặp gỡ trao đổi trực tiếp với Hội đồng Quản trị.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_24h_001",
        "title": "Trưởng Phòng Hành Chính Nhân Sự & Vận Hành - Ngành Sản Xuất",
        "company": "Công ty TNHH Sản Xuất & XNK Linh Kiện Điện Tử",
        "location": "KCN Biên Hòa 2, Đồng Nai / TP. Thủ Đức",
        "salary": "40.000.000 - 52.000.000 VNĐ",
        "source": "Việc Làm 24h (vieclam24h.vn)",
        "posted_date": "Vừa cập nhật",
        "match_score": 95,
        "matching_keywords": ["VIỆC LÀM 24H", "SẢN XUẤT", "ĐỒNG NAI", "ISO 9001", "C&B", "AI HR"],
        "description": "Quản lý toàn diện công tác Vận hành & HCNS nhà máy 500+ công nhân. Điều hành tuyển dụng lao động phổ thông & kỹ sư, cải tiến quy chế lương sản phẩm tăng 12% hiệu suất. Đảm bảo tuân thủ tiêu chuẩn ISO 9001/16949, PCCC và BHXH.",
        "cover_letter": """Kính gửi Ban Giám Đốc Công ty Sản Xuất & XNK Linh Kiện Điện Tử,

Tôi là Nguyễn Văn Duy, từng điều hành HCNS tại KCN Biên Hòa (Công ty Đá Hóa An 1, Nidec-Copal). Tôi có kinh nghiệm thực chiến cải tiến quỹ lương sản phẩm giúp tăng 12% hiệu suất và đạt 0 điểm không tuân thủ trong các kỳ thanh tra ISO/BHXH.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_jobsgo_001",
        "title": "Giám Đốc Nhân Sự & Vận Hành (CHRO / Operations Director)",
        "company": "Tập đoàn Thương Mại & Chuỗi Nhà Hàng F&B Quốc Tế",
        "location": "Quận 1 / Quận 3, TP. Hồ Chí Minh",
        "salary": "50.000.000 - 70.000.000 VNĐ",
        "source": "JobsGO (jobsgo.vn)",
        "posted_date": "Hôm nay",
        "match_score": 94,
        "matching_keywords": ["JOBSGO", "CHRO", "F&B", "TOTAL REWARDS", "BASE.VN", "GEMINI AI"],
        "description": "Quản trị toàn bộ nhân sự và vận hành chuỗi 60+ nhà hàng. Thiết kế chính sách Total Rewards, số hóa chấm công bằng HRIS Base.vn/MISA AMIS và ứng dụng Gemini AI phân tích biến động nhân sự.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Tập đoàn F&B Quốc Tế,

Tôi là Nguyễn Văn Duy, với 15 năm kinh nghiệm quản trị HRIS & Vận hành chuỗi phức tạp. Tôi tiên phong số hóa quy trình Onboarding 90 ngày nâng tỷ lệ giữ chân nhân sự thử việc lên 96%.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_fb_001",
        "title": "COO / Phó Giám Đốc Điều Hành Vận Hành - Ngành Logistics & Supply Chain",
        "company": "Tập đoàn Logistics & Vận Tải Quốc Tế Hàng Hải",
        "location": "Quận 2 / Quận 7, TP. Hồ Chí Minh",
        "salary": "55.000.000 - 75.000.000 VNĐ",
        "source": "Facebook Group (Cộng Đồng HR & Headhunter VN)",
        "posted_date": "Hôm nay",
        "match_score": 93,
        "matching_keywords": ["FACEBOOK GROUP", "COO", "LOGISTICS", "CHỮ KÝ SỐ", "ISO 9001"],
        "description": "Được đăng trực tiếp từ Headhunter uy tín trên Facebook HR Group. Quản lý toàn bộ vận hành văn phòng, đội xe, cảng và nhân sự. Triển khai chữ ký số toàn bộ hợp đồng, rút ngắn 80% thời gian phê duyệt.",
        "cover_letter": """Kính gửi Ban Giám Đốc & Khối Headhunter Tập đoàn Logistics Hàng Hải,

Tôi là Nguyễn Văn Duy, chuyên gia quản trị vận hành & chữ ký số số hóa quy trình. Tôi từng cắt giảm 95% sai sót lưu trữ hợp đồng và tối ưu 15% chi phí hành chính dư thừa.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_24h_002",
        "title": "Trưởng Phòng HCNS Tập Đoàn (HR & Admin Director)",
        "company": "Tập đoàn Đầu Tư Xây Dựng & Năng Lượng Xanh",
        "location": "Quận Bình Thạnh, TP. Hồ Chí Minh",
        "salary": "42.000.000 - 55.000.000 VNĐ",
        "source": "Việc Làm 24h (vieclam24h.vn)",
        "posted_date": "1 ngày trước",
        "match_score": 92,
        "matching_keywords": ["VIỆC LÀM 24H", "XÂY DỰNG", "BSC/KPI GSA", "PMP GOOGLE"],
        "description": "Quản lý 12+ nhân viên phòng HCNS, C&B, Tuyển dụng, L&D. Chủ trì hoạch định nguồn nhân lực công ty mẹ và 3 công ty con, kiểm soát ngân sách lương thưởng và rủi ro pháp lý.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Tập đoàn Xây Dựng & Năng Lượng Xanh,

Tôi là Nguyễn Văn Duy, từng giữ chức Trưởng phòng HCNS Công ty Chấn Hưng (Xây dựng, Kỹ thuật điện). Tôi có bằng Cử nhân HR, chứng chỉ BSC/KPI GSA và chứng chỉ Quản lý Dự án Google.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_jobsgo_002",
        "title": "Giám Đốc Vận Hành & Nhân Sự (Operations & HR Director) - eCommerce",
        "company": "Công ty Cổ phần Công Nghệ Thương Mại Điện Tử & Bán Lẻ",
        "location": "Quận Tân Bình, TP. Hồ Chí Minh",
        "salary": "48.000.000 - 65.000.000 VNĐ",
        "source": "JobsGO (jobsgo.vn)",
        "posted_date": "Hôm nay",
        "match_score": 91,
        "matching_keywords": ["JOBSGO", "ECOMMERCE", "AI AUTOMATION", "GEMINI", "ANTIGRAVITY"],
        "description": "Tối ưu hóa toàn bộ quy trình vận hành kho bãi, nhân sự và CSKH. Ứng dụng các giải pháp Agentic AI (Antigravity 2.0, Gemini Enterprise) tự động hóa báo cáo và Pivot Table dự báo biến động nhân lực.",
        "cover_letter": """Kính gửi Ban Giám Đốc Công ty Công Nghệ TMĐT & Bán Lẻ,

Tôi là Nguyễn Văn Duy, chuyên gia tiên phong ứng dụng Agentic AI (Antigravity 2.0) cắt giảm 75% tác vụ vận hành thủ công và tự động hóa Pivot Table phân tích ngân sách nhân sự.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    }
]

# ========== Custom CSS ==========
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    .stApp {
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #0d9488 100%);
        padding: 1.8rem 2.2rem;
        border-radius: 18px;
        margin-bottom: 1.5rem;
        color: white;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .main-header h1 {
        font-size: 1.8rem;
        font-weight: 800;
        margin: 0;
        color: #f8fafc;
    }

    .main-header p {
        font-size: 0.95rem;
        color: #2dd4bf;
        font-weight: 600;
        margin: 6px 0 0 0;
    }

    .tag {
        display: inline-block;
        background: rgba(59,130,246,0.15);
        color: #93c5fd;
        border: 1px solid rgba(59,130,246,0.25);
        padding: 3px 12px;
        border-radius: 14px;
        font-size: 0.78rem;
        margin-right: 5px;
        margin-bottom: 5px;
        font-weight: 500;
    }

    .source-tag {
        display: inline-block;
        background: rgba(245, 158, 11, 0.15);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.3);
        padding: 2px 10px;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    .stat-box {
        text-align: center;
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 1.1rem;
    }

    .stat-number {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8, #2dd4bf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# ========== Session State ==========
if "jobs" not in st.session_state:
    st.session_state.jobs = EXPANDED_JOBS

if "applied_jobs" not in st.session_state:
    st.session_state.applied_jobs = set()

# ========== Header ==========
st.markdown("""
<div class="main-header">
    <h1>👑 Executive COO & HR Job-Hunt Copilot</h1>
    <p>Đa Nguồn: JobsGO • Việc Làm 24h • Facebook HR Groups • TopCV • VietnamWorks | Dành riêng cho NGUYỄN VĂN DUY</p>
</div>
""", unsafe_allow_html=True)

# ========== Sidebar: Profile ==========
with st.sidebar:
    st.markdown("### 👑 Hồ Sơ Lãnh Đạo")
    st.markdown(f"**{PROFILE['name']}**")
    st.caption(PROFILE['title'])

    st.markdown("---")
    st.markdown("📱 " + PROFILE["contact"]["phone"])
    st.markdown("📧 " + PROFILE["contact"]["email"])
    st.markdown("📍 " + PROFILE["contact"]["location"])
    st.markdown("🔗 " + PROFILE["contact"]["linkedin"])

    st.markdown("---")
    st.markdown("#### 🏅 Năng Lực Vận Hành & HR")
    for skill in PROFILE["skills"][:5]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🎓 Chứng Chỉ C-Level")
    for edu in PROFILE["education"][:4]:
        st.caption(f"• {edu}")

    st.markdown("---")
    st.markdown("#### 🔗 Thông Tin LinkedIn")
    if st.button("📋 Copy Headline COO/HR", use_container_width=True):
        st.code(PROFILE["headline"], language=None)
        st.success("Đã copy Headline!")

    if st.button("📋 Copy About Tóm Tắt", use_container_width=True):
        st.code(PROFILE["summary"], language=None)
        st.success("Đã copy About!")

# ========== Main Content: Stats Row ==========
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{len(st.session_state.jobs)}</div>
        <div>Vị Trí COO & HR Cấp Cao</div>
    </div>""", unsafe_allow_html=True)

with col2:
    coo_count = len([j for j in st.session_state.jobs if "COO" in j["title"] or "Giám Đốc Vận Hành" in j["title"]])
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{coo_count}</div>
        <div>Vị Trí COO (Giám Đốc Vận Hành)</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{len(st.session_state.applied_jobs)}</div>
        <div>Đã Ứng Tuyển</div>
    </div>""", unsafe_allow_html=True)

with col4:
    avg_score = sum(j["match_score"] for j in st.session_state.jobs) // max(len(st.session_state.jobs), 1)
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{avg_score}%</div>
        <div>Match Score Trung Bình</div>
    </div>""", unsafe_allow_html=True)

st.markdown("---")

# ========== Filter Controls ==========
filter_col1, filter_col2 = st.columns([2, 1])

with filter_col1:
    search_keyword = st.text_input("🔍 Tìm kiếm theo vị trí hoặc nguồn (COO, JobsGO, 24h, Facebook, FMCG, BĐS...):", "")

with filter_col2:
    min_score = st.slider("🎯 Độ tương thích Match Score (%):", 70, 98, 85)

# Filter jobs logic
filtered_jobs = [
    j for j in st.session_state.jobs 
    if j["match_score"] >= min_score and 
    (not search_keyword or search_keyword.lower() in (j["title"] + j["company"] + j["source"] + j["description"] + "".join(j["matching_keywords"])).lower())
]

# ========== Job Listings ==========
st.markdown(f"### 🔥 Cơ Hội Việc Làm Lựa Chọn ({len(filtered_jobs)} / {len(st.session_state.jobs)} Vị Trí)")

for idx, job in enumerate(filtered_jobs):
    is_applied = job["id"] in st.session_state.applied_jobs

    with st.container():
        top_col1, top_col2 = st.columns([4, 1])

        with top_col1:
            st.markdown(f"#### {job['title']}")
            st.markdown(f"🏢 **{job['company']}**")

        with top_col2:
            color = "#38bdf8" if "COO" in job["title"] else ("#34d399" if job["match_score"] >= 90 else "#fbbf24")
            st.markdown(f"<div style='text-align:center;'><span style='font-size:1.8rem;font-weight:800;color:{color};'>{job['match_score']}%</span><br><small>Match Score</small></div>", unsafe_allow_html=True)

        meta_col1, meta_col2, meta_col3 = st.columns(3)
        with meta_col1:
            st.caption(f"💰 {job['salary']}")
        with meta_col2:
            st.caption(f"📍 {job['location']}")
        with meta_col3:
            st.markdown(f"<span class='source-tag'>📌 {job['source']}</span>", unsafe_allow_html=True)

        st.caption(job["description"][:260] + "...")

        if job.get("matching_keywords"):
            kw_html = " ".join([f"<span class='tag'>{kw}</span>" for kw in job["matching_keywords"]])
            st.markdown(kw_html, unsafe_allow_html=True)

        btn_col1, btn_col2, btn_col3 = st.columns([1.2, 1.4, 2])

        with btn_col1:
            if is_applied:
                st.success("✅ Đã Nộp Hồ Sơ")
            else:
                if st.button(f"🚀 1-Click Nộp Đơn", key=f"apply_{job['id']}"):
                    st.session_state.applied_jobs.add(job["id"])
                    st.success(f"Đã nộp hồ sơ thành công vị trí {job['title']} tại {job['company']}!")
                    st.rerun()

        with btn_col2:
            if st.button(f"📝 Cover Letter COO/HR", key=f"cl_{job['id']}"):
                st.session_state[f"show_cl_{job['id']}"] = not st.session_state.get(f"show_cl_{job['id']}", False)

        if st.session_state.get(f"show_cl_{job['id']}", False):
            with st.expander(f"Thư Ứng Tuyển Cá Nhân Hóa - {job['company']}", expanded=True):
                edited_letter = st.text_area(
                    "Chỉnh sửa Cover Letter trước khi gửi:",
                    value=job["cover_letter"],
                    height=280,
                    key=f"letter_{job['id']}"
                )
                if st.button(f"💾 Lưu & Nộp Hồ Sơ", key=f"save_cl_{job['id']}"):
                    job["cover_letter"] = edited_letter
                    st.session_state.applied_jobs.add(job["id"])
                    st.success("Đã nộp đơn thành công!")
                    st.rerun()

        st.markdown("---")

st.caption("Executive COO & HR Job-Hunt Copilot © 2026 | Powered by Gemini AI & Antigravity 2.0 | Nguyễn Văn Duy")
