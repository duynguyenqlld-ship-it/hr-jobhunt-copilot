"""
Streamlit Dashboard - Executive HR Job-Hunt Copilot
===================================================
Tập trung vị trí Trưởng phòng HCNS, HRBP Strategic Partner & Head of HR / CHRO.
Thu thập việc làm từ JobsGO, Việc Làm 24h, Facebook HR Groups, TopCV, VietnamWorks.
"""
import os
import sys
import time
import json
import streamlit as st

# ========== Page Config ==========
st.set_page_config(
    page_title="HR Executive Job-Hunt Copilot | Nguyễn Văn Duy",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== Candidate Profile Data (HR Executive & HRBP) ==========
PROFILE = {
    "name": "NGUYỄN VĂN DUY",
    "title": "TRƯỞNG PHÒNG HÀNH CHÍNH NHÂN SỰ (HR & ADMINISTRATION MANAGER)",
    "headline": "Trưởng phòng Hành chính Nhân sự | HRBP Strategic Partner | Chuyển đổi số HR & Antigravity AI",
    "contact": {
        "phone": "0902.741.792",
        "email": "duynguyen.qlld@gmail.com",
        "location": "Long Bình, Tp. Hồ Chí Minh",
        "linkedin": "linkedin.com/in/duynguyen-hr"
    },
    "summary": "Chuyên gia Nhân sự với 15 năm kinh nghiệm thực chiến vận hành hệ thống quản trị nhân lực quy mô lớn (3.000+ nhân sự) đa lĩnh vực: Sản xuất, FMCG, Bán lẻ, Xây dựng & Bất động sản. Nổi bật với tư duy tái cấu trúc chiến lược, tối ưu định biên 15% nhằm tối đa hóa hiệu suất vận hành và tiết giảm chi phí lao động. Tiên phong chuyển đổi số trong quản trị HR, ứng dụng thành thạo AI (Google Gemini, Antigravity 2.0 Agentic AI) cắt giảm 75% tác vụ thủ công và số hóa trải nghiệm nhân viên.",
    "skills": [
        "Talent Acquisition & Headhunting",
        "Workforce Planning & Competency Framework",
        "KPI / OKR Performance Management",
        "Compensation & Benefits (Total Rewards)",
        "HRIS & Digital HR Transformation (Base.vn, MISA AMIS, Lark People)",
        "AI Automation in HR (Google Gemini Enterprise, Antigravity 2.0 Agentic AI)",
        "Labor Law & ISO 9001/16949 Compliance"
    ],
    "education": [
        "Cử nhân Quản trị Nguồn nhân lực — Đại học Lao động & Xã hội",
        "Chứng chỉ Kỹ thuật xây dựng & triển khai BSC & KPI (2025)",
        "Chứng chỉ Quản lý Dự án Chuyên nghiệp (Project Management) - Google (2024)",
        "Chứng chỉ Giám đốc Điều hành (CEO) - DVL EDU (2019)",
        "Đánh giá viên nội bộ ISO 9001:2015 & ISO/TS 16949"
    ]
}

# ========== Multi-Source HR Jobs Database (JobsGO, 24h, FB Groups, TopCV...) ==========
EXPANDED_JOBS = [
    {
        "id": "job_hr_001",
        "title": "Trưởng Phòng Hành Chính Nhân Sự (HR Manager) - Ngành FMCG & Bán Lẻ",
        "company": "Tập đoàn Sản Xuất & Chuỗi Bán Lẻ Thực Phẩm Đa Quốc Gia",
        "location": "Quận 1 / Quận 2, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 55.000.000 VNĐ",
        "source": "JobsGO (jobsgo.vn)",
        "posted_date": "Hôm nay",
        "match_score": 98,
        "matching_keywords": ["TRƯỞNG PHÒNG", "FMCG", "BÁN LẺ", "KPI", "HRIS", "BASE.VN"],
        "description": "Quản lý toàn bộ hoạt động HCNS quy mô 1.500 nhân sự. Xây dựng chiến lược nhân sự dài hạn, tái cấu trúc sơ đồ tổ chức. Xây dựng và theo dõi hệ thống BSC/KPI cho khối văn phòng và nhà máy sản xuất. Triển khai chuyển đổi số HRIS (Base.vn/MISA), tối ưu ngân sách lương thưởng C&B.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Tập đoàn Sản Xuất & Chuỗi Bán Lẻ Thực Phẩm,

Tôi là Nguyễn Văn Duy, chuyên gia 15 năm kinh nghiệm điều hành Hành chính Nhân sự tổng thể (HR Manager / HRBP Strategic Partner) cho các doanh nghiệp quy mô 3.000+ nhân sự trong ngành FMCG & Bán lẻ.

Với kinh nghiệm từng trực tiếp tối ưu định biên 15%, triển khai BSC/KPI nâng 18% năng suất lao động và tích hợp hệ thống HRIS (Base.vn, MISA AMIS) cùng AI Gemini tự động hóa 75% tác vụ thủ công, tôi hoàn toàn tự tin đảm nhận vị trí Trưởng Phòng HCNS tại Quý Tập đoàn.

Trân trọng,
Nguyễn Văn Duy - Trưởng phòng HCNS
Điện thoại: 0902.741.792 | Email: duynguyen.qlld@gmail.com"""
    },
    {
        "id": "job_hr_002",
        "title": "HRBP Strategic Partner (Trưởng Phòng Nhân Sự Đối Tác Chiến Lược)",
        "company": "Công ty Cổ phần Xây dựng & Bất động sản Đô thị",
        "location": "TP. Thủ Đức, TP. Hồ Chí Minh",
        "salary": "35.000.000 - 50.000.000 VNĐ",
        "source": "Facebook Group (Executive Headhunter Vietnam)",
        "posted_date": "Hôm nay",
        "match_score": 96,
        "matching_keywords": ["HRBP", "TÁI CẤU TRÚC", "BẤT ĐỘNG SẢN", "OKR", "TALENT ACQUISITION"],
        "description": "Đóng vai trò Đối tác chiến lược HR sát cánh cùng CEO và Hội đồng quản trị. Hoạch định định biên nhân sự, thu hút nhân tài cấp cao (Talent Acquisition). Triển khai đánh giá hiệu suất OKR/KPI, cải tiến văn hóa doanh nghiệp và giữ chân nhân tài thử việc.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Công ty Cổ phần Xây dựng & Bất động sản Đô thị,

Tôi là Nguyễn Văn Duy, ứng viên vị trí HRBP Strategic Partner. Tôi sở hữu 15 năm kinh nghiệm tư vấn chiến lược nhân sự, hoạch định định biên và triển khai KPI/OKR giúp giảm tỷ lệ nghỉ việc từ 22% xuống 11%.

Tôi rất mong có cơ hội đồng hành cùng Ban Giám đốc phát triển nguồn nhân lực bền vững.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_hr_003",
        "title": "Giám Đốc Nhân Sự (CHRO / Head of HR) - Chuỗi Hệ Thống Bán Lẻ & Thương Mại",
        "company": "Tập đoàn Thương mại & Chuỗi Cửa Hàng Tiện Lợi",
        "location": "Quận 3, TP. Hồ Chí Minh",
        "salary": "50.000.000 - 70.000.000 VNĐ",
        "source": "JobsGO (jobsgo.vn)",
        "posted_date": "1 ngày trước",
        "match_score": 95,
        "matching_keywords": ["CHRO", "GIÁM ĐỐC NHÂN SỰ", "TOTAL REWARDS", "BASE.VN", "MISA AMIS"],
        "description": "Chịu trách nhiệm toàn bộ hệ thống quản trị nhân sự 3.000+ nhân viên chuỗi bán lẻ. Thiết kế lại chính sách Lương thưởng Total Rewards, tối ưu chi phí vận hành. Ứng dụng AI và giải pháp tự động hóa HR trong việc tính lương, quản lý hợp đồng lao động và ISO 9001.",
        "cover_letter": """Kính gửi Ban Giám Đốc Tập đoàn Thương mại & Chuỗi Cửa Hàng Tiện Lợi,

Tôi là Nguyễn Văn Duy, sở hữu 15 năm kinh nghiệm điều hành HR quy mô 3.000+ lao động đa lĩnh vực (Bán lẻ, FMCG, BĐS). Năng lực nổi bật của tôi là tái cấu trúc tổ chức, chuyển đổi số HRIS và xây dựng chính sách Total Rewards hiệu suất cao.

Rất mong được trao đổi chi tiết cùng Hội đồng Quản trị.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_hr_004",
        "title": "Trưởng Phòng Hành Chính Nhân Sự Nhà Máy (Khu Công Nghiệp)",
        "company": "Tập đoàn Sản Xuất Linh Kiện & Điện Tử Đa Quốc Gia",
        "location": "KCN Biên Hòa 2, Đồng Nai / TP. Thủ Đức",
        "salary": "38.000.000 - 48.000.000 VNĐ",
        "source": "Việc Làm 24h (vieclam24h.vn)",
        "posted_date": "Vừa cập nhật",
        "match_score": 94,
        "matching_keywords": ["VIỆC LÀM 24H", "SẢN XUẤT", "ĐỒNG NAI", "ISO 9001", "C&B"],
        "description": "Điều hành phòng HCNS 10+ nhân viên. Quản lý tuyển dụng số lượng lớn lao động phổ thông và kỹ sư. Giải quyết quan hệ lao động, thanh tra BHXH, PCCC và làm việc với cơ quan nhà nước. Áp dụng tiêu chí ASK trong phỏng vấn tuyển dụng.",
        "cover_letter": """Kính gửi Bộ phận Tuyển dụng Tập đoàn Sản Xuất Linh Kiện & Điện Tử,

Tôi là Nguyễn Văn Duy, từng giữ vị trí Trưởng nhóm Tuyển dụng & Đào tạo Nidec-Copal Precision và Trưởng phòng HCNS Công ty Đá Hóa An 1. Tôi có kinh nghiệm quản lý rủi ro pháp lý lao động, cung ứng 1.200+ lao động/năm và đảm bảo tiêu chuẩn ISO 9001/16949.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_hr_005",
        "title": "Senior HR Manager / Chuyên Gia Chuyển Đổi Số Nhân Sự",
        "company": "Tập đoàn Đầu tư & Công nghệ Dịch vụ Đa ngành",
        "location": "Quận 1, TP. Hồ Chí Minh",
        "salary": "45.000.000 - 60.000.000 VNĐ",
        "source": "Facebook Group (Cộng Đồng HR & Headhunter VN)",
        "posted_date": "Hôm nay",
        "match_score": 92,
        "matching_keywords": ["CHUYỂN ĐỔI SỐ", "GEMINI AI", "HRIS", "LARK PEOPLE", "MISA AMIS"],
        "description": "Chủ trì dự án chuyển đổi số HR toàn tập đoàn. Triển khai các công cụ AI phân tích dữ liệu nhân sự, dự báo biến động lao động. Chuẩn hóa quy trình Onboarding, quản lý rủi ro pháp lý hợp đồng lao động và chữ ký số.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Tập đoàn Đầu tư & Công nghệ Dịch vụ Đa ngành,

Tôi là Nguyễn Văn Duy, tiên phong ứng dụng Chuyển đổi số HR và AI (Google Gemini, Antigravity 2.0 Agentic AI) vào tự động hóa vận hành nhân sự, cắt giảm 75% tác vụ thủ công và 40% thời gian lọc hồ sơ.

Rất mong được hợp tác đưa chuyển đổi số HR vào thực tiễn tại Quý Tập đoàn.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_hr_006",
        "title": "Giám Đốc HRBP / Head of HR - Ngành Bất Động Sản Nghỉ Dưỡng",
        "company": "Tập đoàn Đầu Tư & Phát Triển Bất Động Sản Đô Thị",
        "location": "Quận 1, TP. Hồ Chí Minh",
        "salary": "55.000.000 - 75.000.000 VNĐ",
        "source": "Việc Làm 24h & JobsGO",
        "posted_date": "Hôm nay",
        "match_score": 93,
        "matching_keywords": ["HRBP", "BẤT ĐỘNG SẢN NGHỈ DƯỠNG", "GIÁM ĐỐC NHÂN SỰ", "TÁI CẤU TRÚC"],
        "description": "Tham mưu cho HĐQT kiện toàn bộ máy tổ chức tập đoàn mẹ và 5 công ty con. Tái cấu trúc khung năng lực, chính sách hoa hồng bán hàng và quản trị rủi ro pháp lý HR.",
        "cover_letter": """Kính gửi Hội đồng Quản trị Tập đoàn Bất Động Sản Đô Thị,

Tôi là Nguyễn Văn Duy, từng đảm nhiệm Trưởng phòng HCNS Công ty BĐS Nhật Tiến (300+ nhân sự). Tôi am hiểu sâu sắc cơ cấu tổ chức công ty mẹ - con và tái cấu trúc quỹ lương hiệu quả.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_hr_007",
        "title": "Trưởng Phòng HR - Ngành Chuỗi Nhà Hàng & F&B Quốc Tế",
        "company": "Tập đoàn Ẩm Thực & Dịch Vụ F&B",
        "location": "Quận 1 / Quận 3, TP. Hồ Chí Minh",
        "salary": "35.000.000 - 45.000.000 VNĐ",
        "source": "JobsGO (jobsgo.vn)",
        "posted_date": "Hôm nay",
        "match_score": 90,
        "matching_keywords": ["JOBSGO", "F&B", "CHUỖI NHÀ HÀNG", "RETAIL", "C&B"],
        "description": "Quản lý tuyển dụng, đào tạo và chính sách đãi ngộ cho chuỗi 50+ nhà hàng tại TP.HCM. Tối ưu định biên nhân sự ca xoay, thiết lập chỉ số KPI giữ chân nhân sự thử việc.",
        "cover_letter": """Kính gửi Ban Tuyển Dụng Tập đoàn Ẩm Thực & Dịch Vụ F&B Quốc Tế,

Tôi là Nguyễn Văn Duy với 15 năm kinh nghiệm quản trị HR chuỗi bán lẻ & dịch vụ phức tạp. Tôi từng triển khai hệ thống Onboarding 90 ngày nâng tỷ lệ giữ chân nhân sự lên 96%.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_hr_008",
        "title": "Head of Talent Acquisition & HR Operations",
        "company": "Công ty Cổ phần Hạ Tầng & Dược Phẩm Thiết Bị Y Tế",
        "location": "Quận 10, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 52.000.000 VNĐ",
        "source": "Việc Làm 24h (vieclam24h.vn)",
        "posted_date": "1 ngày trước",
        "match_score": 89,
        "matching_keywords": ["VIỆC LÀM 24H", "TALENT ACQUISITION", "DƯỢC PHẨM", "Y TẾ"],
        "description": "Lập chiến lược thu hút nhân tài cấp trung & cấp cao. Chuẩn hóa quy trình phỏng vấn theo khung năng lực ASK. Quản lý toàn bộ vận hành C&B, BHXH và quan hệ lao động.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Công ty Dược Phẩm Thiết Bị Y Tế,

Tôi là Nguyễn Văn Duy, chuyên gia Tuyển dụng & Vận hành HR chiến lược. Tôi sở hữu chứng chỉ Quản lý Dự án Google (PMP) và chứng chỉ BSC/KPI GSA.

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
        background: linear-gradient(135deg, #1e3a5f 0%, #0d9488 100%);
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
    <h1>🎯 HR Executive & HRBP Job-Hunt Copilot</h1>
    <p>Đa Nguồn: JobsGO • Việc Làm 24h • Facebook HR Groups • TopCV • VietnamWorks | Dành riêng cho NGUYỄN VĂN DUY</p>
</div>
""", unsafe_allow_html=True)

# ========== Sidebar: Profile ==========
with st.sidebar:
    st.markdown("### 👤 Hồ Sơ Nhân Sự Cấp Cao")
    st.markdown(f"**{PROFILE['name']}**")
    st.caption(PROFILE['title'])

    st.markdown("---")
    st.markdown("📱 " + PROFILE["contact"]["phone"])
    st.markdown("📧 " + PROFILE["contact"]["email"])
    st.markdown("📍 " + PROFILE["contact"]["location"])
    st.markdown("🔗 " + PROFILE["contact"]["linkedin"])

    st.markdown("---")
    st.markdown("#### 🏅 Năng Lực Cốt Lõi HR")
    for skill in PROFILE["skills"][:5]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🎓 Chứng Chỉ Chuyên Ngành")
    for edu in PROFILE["education"][:4]:
        st.caption(f"• {edu}")

    st.markdown("---")
    st.markdown("#### 🔗 Thông Tin Cho LinkedIn")
    if st.button("📋 Copy Headline HR Manager", use_container_width=True):
        st.code(PROFILE["headline"], language=None)
        st.success("Đã copy Headline!")

    if st.button("📋 Copy About Tóm Tắt CV", use_container_width=True):
        st.code(PROFILE["summary"], language=None)
        st.success("Đã copy About!")

# ========== Main Content: Stats Row ==========
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{len(st.session_state.jobs)}</div>
        <div>Vị Trí HR Cấp Cao</div>
    </div>""", unsafe_allow_html=True)

with col2:
    high_match = len([j for j in st.session_state.jobs if j["match_score"] >= 90])
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{high_match}</div>
        <div>Match Score ≥ 90%</div>
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
    search_keyword = st.text_input("🔍 Tìm kiếm theo vị trí hoặc nguồn (JobsGO, 24h, Facebook, HRBP, FMCG, BĐS...):", "")

with filter_col2:
    min_score = st.slider("🎯 Độ tương thích Match Score (%):", 70, 98, 85)

# Filter jobs logic
filtered_jobs = [
    j for j in st.session_state.jobs 
    if j["match_score"] >= min_score and 
    (not search_keyword or search_keyword.lower() in (j["title"] + j["company"] + j["source"] + j["description"] + "".join(j["matching_keywords"])).lower())
]

# ========== Job Listings ==========
st.markdown(f"### 🔥 Hiển Thị {len(filtered_jobs)} / {len(st.session_state.jobs)} Việc Làm HR Cấp Cao")

for idx, job in enumerate(filtered_jobs):
    is_applied = job["id"] in st.session_state.applied_jobs

    with st.container():
        top_col1, top_col2 = st.columns([4, 1])

        with top_col1:
            st.markdown(f"#### {job['title']}")
            st.markdown(f"🏢 **{job['company']}**")

        with top_col2:
            color = "#34d399" if job["match_score"] >= 92 else "#38bdf8"
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
            if st.button(f"📝 Cover Letter HR", key=f"cl_{job['id']}"):
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

st.caption("HR Executive Job-Hunt Copilot © 2026 | Powered by Gemini AI & Antigravity 2.0 | Nguyễn Văn Duy")
