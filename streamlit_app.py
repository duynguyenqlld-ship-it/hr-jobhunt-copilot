"""
Streamlit Dashboard - HR Executive Job-Hunt Copilot
====================================================
Giao diện web chuyên nghiệp chạy trên Streamlit Cloud.
Tích hợp sẵn bộ trích xuất CV, AI Matcher & Danh sách việc làm.
"""
import os
import sys
import time
import json
import streamlit as st

# ========== Page Config ==========
st.set_page_config(
    page_title="HR Job-Hunt Copilot | Nguyễn Văn Duy",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== Candidate Profile Data ==========
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
    "summary": "Chuyên gia Nhân sự với 15 năm kinh nghiệm thực chiến vận hành hệ thống quản trị nhân lực quy mô lớn (3.000+ nhân sự) đa lĩnh vực: Sản xuất, FMCG, Bán lẻ, Xây dựng & Bất động sản. Nổi bật với tư duy tái cấu trúc chiến lược, tối ưu định biên nhằm tối đa hóa hiệu suất vận hành và tiết giảm chi phí lao động. Tiên phong chuyển đổi số trong quản trị HR, ứng dụng thành thạo AI (Google Gemini, Antigravity 2.0 Agentic AI) để tinh gọn quy trình và số hóa trải nghiệm nhân viên.",
    "experiences": [
        {
            "title": "TRƯỞNG PHÒNG HÀNH CHÍNH NHÂN SỰ",
            "company": "Ngành: Sản xuất – Thương mại FMCG & Bán lẻ",
            "period": "08/2025 – NAY",
            "achievements": [
                "Thiết kế lại sơ đồ tổ chức, tinh gọn 15% định biên hành chính dư thừa",
                "Xây dựng BSC & KPI chuẩn GSA, nâng 18% năng suất lao động toàn doanh nghiệp",
                "Tái cấu trúc thương hiệu nhà tuyển dụng, rút ngắn thời gian tuyển dụng từ 35 xuống 18 ngày",
                "Triển khai tích hợp HRIS (Base.vn, MISA AMIS) xử lý chấm công tự động",
                "Ứng dụng Gemini AI & Antigravity 2.0 giảm 75% khối lượng tác vụ giải đáp thủ công phòng HR"
            ]
        },
        {
            "title": "TRƯỞNG PHÒNG HÀNH CHÍNH NHÂN SỰ",
            "company": "Công ty Cổ phần TM Kỹ thuật DV Chấn Hưng",
            "period": "2023 – 08/2025",
            "achievements": [
                "Hoạch định nguồn nhân lực & quản lý 8 nhân viên chuyên môn (Lễ tân, HC, Tuyển dụng, L&D, C&B, IT)",
                "Số hóa tuyển dụng bằng AI: cắt giảm 40% thời gian lọc hồ sơ, nâng tỷ lệ vượt thử việc lên 92%",
                "Tự động hóa tính lương & phân tích dữ liệu bằng Gemini trên Google Sheets, làm sạch dữ liệu 200+ nhân sự",
                "Triển khai chữ ký số toàn bộ hợp đồng lao động, rút ngắn 80% thời gian phê duyệt"
            ]
        },
        {
            "title": "TRƯỞNG PHÒNG HÀNH CHÍNH NHÂN SỰ",
            "company": "Công ty Cổ phần ĐT TM Nhật Tiến",
            "period": "2019 – 2023",
            "achievements": [
                "Triển khai KPI kết hợp OKR cho 300 nhân sự, nâng 15% năng suất lao động",
                "Giảm tỷ lệ nghỉ việc từ 22% xuống 11% trong 18 tháng",
                "Tái thiết kế Onboarding 90 ngày, nâng tỷ lệ giữ chân thử việc lên 96%"
            ]
        }
    ],
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
        "Chứng chỉ Quản lý Dự án Chuyên nghiệp - Google (2024)",
        "Chứng chỉ Giám đốc Điều hành (CEO) - DVL EDU (2019)",
        "Đánh giá viên nội bộ ISO 9001:2015 & ISO/TS 16949"
    ]
}

# ========== Curated Job Opportunities ==========
SAMPLE_JOBS = [
    {
        "id": "job_001",
        "title": "Trưởng Phòng Hành Chính Nhân Sự (HR Manager) - Ngành FMCG & Bán Lẻ",
        "company": "Tập đoàn Bán lẻ & Sản xuất Thực phẩm Quốc tế",
        "location": "Quận 1 / Quận 2, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 55.000.000 VNĐ",
        "source": "TopCV / VietnamWorks",
        "posted_date": "Hôm nay",
        "match_score": 96,
        "matching_keywords": ["TRƯỞNG PHÒNG", "FMCG", "BÁN LẺ", "KPI", "HRIS", "BASE.VN"],
        "description": "Quản lý toàn bộ hoạt động HCNS quy mô 1.500 nhân sự. Xây dựng chiến lược nhân sự dài hạn, tái cấu trúc sơ đồ tổ chức. Xây dựng và theo dõi hệ thống BSC/KPI cho khối văn phòng và nhà máy sản xuất. Triển khai chuyển đổi số HRIS (Base.vn/MISA), tối ưu ngân sách lương thưởng C&B.",
        "cover_letter": """Kính gửi Ban Lãnh đạo và Bộ phận Tuyển dụng Tập đoàn Bán lẻ & Sản xuất Thực phẩm Quốc tế,

Tôi là Nguyễn Văn Duy, với 15 năm kinh nghiệm thực chiến trong quản trị nhân sự tổng thể (HR Manager / HRBP Strategic Partner) cho các tập đoàn và doanh nghiệp quy mô lớn từ 200 đến hơn 3.000 nhân sự. Tôi rất hào hứng khi biết Quý Công ty đang tìm kiếm vị trí Trưởng Phòng Hành Chính Nhân Sự (HR Manager) - Ngành FMCG & Bán Lẻ.

Qua tìm hiểu về mô tả công việc, tôi tin rằng năng lực và kinh nghiệm của mình hoàn toàn đáp ứng xuất sắc các yêu cầu mà Công ty đang kỳ vọng:

1. Tái cấu trúc & Quản trị chiến lược: Tôi từng trực tiếp tối ưu định biên 15%, thiết kế hệ thống BSC & KPI giúp nâng 18% năng suất lao động và rút ngắn thời gian tuyển dụng từ 35 xuống 18 ngày.
2. Tiên phong Chuyển đổi số & AI HR: Triển khai thành công các hệ thống HRIS (Base.vn, MISA AMIS, Lark People) và ứng dụng thành thạo Google Gemini AI / Antigravity Agentic AI để tự động hóa 75% tác vụ vận hành nhân sự thủ công.
3. Am hiểu sâu sắc đa ngành & Pháp lý lao động: Dày dạn kinh nghiệm điều hành HR trong các lĩnh vực Sản xuất, FMCG, Bán lẻ, Bất động sản & Xây dựng; đảm bảo tuân thủ tuyệt đối ISO 9001/16949 và pháp luật lao động.

Với tư duy hướng tới hiệu quả chi phí và tạo dựng văn hóa làm việc hiệu suất cao, tôi rất mong có cơ hội được trao đổi trực tiếp cùng Ban Lãnh đạo để chia sẻ cụ thể hơn về chiến lược phát triển nguồn nhân lực cho Quý Công ty.

Trân trọng,
Nguyễn Văn Duy
Trưởng phòng Hành chính Nhân sự
Điện thoại: 0902.741.792 | Email: duynguyen.qlld@gmail.com
LinkedIn: linkedin.com/in/duynguyen-hr"""
    },
    {
        "id": "job_002",
        "title": "HRBP Strategic Partner (Trưởng Phòng Nhân Sự Đối Tác Chiến Lược)",
        "company": "Công ty Cổ phần Xây dựng & Bất động sản Đô thị",
        "location": "TP. Thủ Đức, TP. Hồ Chí Minh",
        "salary": "35.000.000 - 50.000.000 VNĐ",
        "source": "LinkedIn Jobs",
        "posted_date": "1 ngày trước",
        "match_score": 92,
        "matching_keywords": ["HRBP", "TÁI CẤU TRÚC", "BẤT ĐỘNG SẢN", "OKRS", "TALENT ACQUISITION"],
        "description": "Đóng vai trò Đối tác chiến lược HR sát cánh cùng CEO và Hội đồng quản trị. Hoạch định định biên nhân sự, thu hút nhân tài cấp cao (Talent Acquisition). Triển khai đánh giá hiệu suất OKR/KPI, cải tiến văn hóa doanh nghiệp và giữ chân nhân tài thử việc.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Công ty Cổ phần Xây dựng & Bất động sản Đô thị,

Tôi là Nguyễn Văn Duy, chuyên gia Nhân sự cấp cao với 15 năm kinh nghiệm điều hành HR chiến lược. Tôi rất quan tâm đến vị trí HRBP Strategic Partner tại Quý Công ty.

Với kinh nghiệm từng triển khai thành công hệ thống OKR/KPI cho 300+ nhân sự, xây dựng khung năng lực và giảm tỷ lệ nghỉ việc từ 22% xuống 11%, tôi tin tưởng sẽ đồng hành hiệu quả cùng Ban Giám đốc tối ưu hóa bộ máy vận hành và thu hút nhân tài cấp cao.

Tôi rất mong có cơ hội trao đổi trực tiếp với Quý Công ty.

Trân trọng,
Nguyễn Văn Duy
SĐT: 0902.741.792 | Email: duynguyen.qlld@gmail.com"""
    },
    {
        "id": "job_003",
        "title": "Giám Đốc Nhân Sự (Head of HR) - Chuỗi Hệ Thống Bán Lẻ & Thương Mại",
        "company": "Tập đoàn Thương mại & Chuỗi Cửa Hàng Tiện Lợi",
        "location": "Quận 3, TP. Hồ Chí Minh",
        "salary": "50.000.000 - 70.000.000 VNĐ",
        "source": "CareerBuilder",
        "posted_date": "2 ngày trước",
        "match_score": 88,
        "matching_keywords": ["HEAD OF HR", "GIÁM ĐỐC NHÂN SỰ", "TOTAL REWARDS", "CHUYỂN ĐỔI SỐ"],
        "description": "Chịu trách nhiệm toàn bộ hệ thống quản trị nhân sự 3.000+ nhân viên chuỗi bán lẻ. Thiết kế lại chính sách Lương thưởng Total Rewards, tối ưu chi phí vận hành. Ứng dụng AI và giải pháp tự động hóa HR trong việc tính lương, quản lý hợp đồng lao động và ISO 9001.",
        "cover_letter": """Kính gửi Ban Giám Đốc Tập đoàn Thương mại & Chuỗi Cửa Hàng Tiện Lợi,

Tôi là Nguyễn Văn Duy, ứng viên vị trí Giám Đốc Nhân Sự (Head of HR). Tôi sở hữu 15 năm kinh nghiệm quản trị hệ thống HR quy mô 3.000+ nhân sự trong ngành Bán lẻ & FMCG.

Thế mạnh của tôi nằm ở năng lực tái cấu trúc sơ đồ tổ chức, tối ưu chi phí nhân công và ứng dụng công nghệ AI / HRIS (Base.vn, MISA) vào tự động hóa vận hành.

Rất mong được gặp gỡ và trao đổi cùng Hội đồng Quản trị.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_004",
        "title": "Trưởng Phòng Hành Chính Nhân Sự Nhà Máy (Khu Công Nghiệp)",
        "company": "Công ty TNHH Sản Xuất Linh Kiện & Điện Tử Multi-National",
        "location": "Khu Công Nghiệp Biên Hòa 2, Đồng Nai / TP. Thủ Đức",
        "salary": "38.000.000 - 48.000.000 VNĐ",
        "source": "ITViec / TopCV",
        "posted_date": "Hôm nay",
        "match_score": 85,
        "matching_keywords": ["SẢN XUẤT", "NHÀ MÁY", "QUAN HỆ LAO ĐỘNG", "ISO 9001", "C&B"],
        "description": "Điều hành phòng HCNS 10+ nhân viên. Quản lý tuyển dụng số lượng lớn lao động phổ thông và kỹ sư. Giải quyết quan hệ lao động, thanh tra BHXH, PCCC và làm việc với cơ quan nhà nước. Áp dụng tiêu chí ASK trong phỏng vấn tuyển dụng.",
        "cover_letter": """Kính gửi Bộ phận Tuyển dụng Công ty TNHH Sản Xuất Linh Kiện & Điện Tử Multi-National,

Tôi là Nguyễn Văn Duy, Trưởng phòng HCNS với 15 năm kinh nghiệm quản lý HR nhà máy sản xuất (Nidec-Copal, Đá Hóa An 1).

Tôi có kinh nghiệm chuyên sâu về quản lý rủi ro pháp lý lao động, làm việc với cơ quan chức năng, tuân thủ ISO 9001/16949 và cung ứng 1.200+ lao động/năm.

Rất mong được hợp tác cùng Quý Công ty.

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

# ========== Session State ==========
if "jobs" not in st.session_state:
    st.session_state.jobs = SAMPLE_JOBS

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
    st.markdown(f"**{PROFILE['name']}**")
    st.caption(PROFILE['title'])

    st.markdown("---")
    st.markdown("📱 " + PROFILE["contact"]["phone"])
    st.markdown("📧 " + PROFILE["contact"]["email"])
    st.markdown("📍 " + PROFILE["contact"]["location"])
    st.markdown("🔗 " + PROFILE["contact"]["linkedin"])

    st.markdown("---")
    st.markdown("#### 🏅 Năng Lực Cốt Lõi")
    for skill in PROFILE["skills"][:5]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🎓 Bằng Cấp & Chứng Chỉ")
    for edu in PROFILE["education"][:3]:
        st.caption(f"• {edu}")

    st.markdown("---")
    st.markdown("#### 🔗 Thông Tin Cho LinkedIn")
    if st.button("📋 Copy Headline", use_container_width=True):
        st.code(PROFILE["headline"], language=None)
        st.success("Đã sẵn sàng copy!")

    if st.button("📋 Copy About", use_container_width=True):
        st.code(PROFILE["summary"], language=None)
        st.success("Đã sẵn sàng copy!")

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

        st.caption(job["description"][:220] + "...")

        if job.get("matching_keywords"):
            kw_html = " ".join([f"<span class='tag'>{kw}</span>" for kw in job["matching_keywords"]])
            st.markdown(kw_html, unsafe_allow_html=True)

        btn_col1, btn_col2, btn_col3 = st.columns([1.2, 1.2, 2])

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

        if st.session_state.get(f"show_cl_{job['id']}", False):
            with st.expander(f"Cover Letter - {job['company']}", expanded=True):
                edited_letter = st.text_area(
                    "Chỉnh sửa Cover Letter trước khi nộp:",
                    value=job["cover_letter"],
                    height=280,
                    key=f"letter_{job['id']}"
                )
                if st.button(f"💾 Lưu & Nộp Đơn", key=f"save_cl_{job['id']}"):
                    job["cover_letter"] = edited_letter
                    st.session_state.applied_jobs.add(job["id"])
                    st.success("Đã lưu Cover Letter và nộp hồ sơ thành công!")
                    st.rerun()

        st.markdown("---")

st.caption("HR Executive Job-Hunt Copilot © 2026 | AI-Powered by Gemini & Antigravity | Dành cho Nguyễn Văn Duy")
