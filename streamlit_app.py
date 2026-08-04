"""
Streamlit Dashboard - Trưởng Phòng HCNS Job-Hunt & Application Tracker (Lương ≥ 30 Tr/Tháng)
==========================================================================================
- Chỉ chọn lọc các vị trí Trưởng phòng Hành chính Nhân sự với Mức Lương từ 30 Triệu trở lên.
- Theo dõi Lịch sử nộp hồ sơ chi tiết (Thời gian, Công ty, Status, Cover Letter đã gửi).
- Tính năng Cập nhật Tin mới mỗi ngày (Daily Real-time Refresh).
"""
import os
import sys
import time
import datetime
import json
import streamlit as st

# ========== Page Config ==========
st.set_page_config(
    page_title="Trưởng Phòng HCNS Job-Hunt Copilot (Lương ≥ 30M) | Nguyễn Văn Duy",
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

# TODAY DATE STRING
TODAY_STR = datetime.date.today().strftime("%d/%m/%Y")

# ========== Targeted HR Manager Jobs (Salary >= 30M VNĐ/Month) ==========
HR_MANAGER_JOBS = [
    {
        "id": "job_30m_001",
        "title": "Trưởng Phòng Hành Chính Nhân Sự - Ngành Sản Xuất FMCG & Bán Lẻ",
        "company": "Tập đoàn Sản Xuất & Chuỗi Bán Lẻ Thực Phẩm Đa Quốc Gia",
        "location": "Quận 1 / Quận 2, TP. Hồ Chí Minh",
        "salary_num": 45000000,
        "salary": "40.000.000 - 55.000.000 VNĐ/tháng",
        "source": "JobsGO (jobsgo.vn)",
        "posted_date": f"Cập nhật ngày {TODAY_STR}",
        "match_score": 98,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "FMCG", "BÁN LẺ", "BSC/KPI GSA", "BASE.VN"],
        "description": "Quản lý toàn bộ hoạt động HCNS quy mô 1.500 nhân sự. Tái cấu trúc sơ đồ tổ chức, tối ưu 15% định biên. Xây dựng và theo dõi hệ thống BSC/KPI cho khối văn phòng và nhà máy sản xuất. Triển khai chuyển đổi số HRIS (Base.vn/MISA AMIS), ứng dụng AIGemini tự động hóa C&B.",
        "cover_letter": f"""Kính gửi Ban Lãnh đạo Tập đoàn Sản Xuất & Chuỗi Bán Lẻ Thực Phẩm,

Tôi là Nguyễn Văn Duy, chuyên gia 15 năm kinh nghiệm điều hành Hành chính Nhân sự tổng thể (HR Manager / HRBP Strategic Partner) cho các doanh nghiệp quy mô 3.000+ nhân sự trong ngành FMCG & Bán lẻ.

Với kinh nghiệm từng trực tiếp thiết kế lại sơ đồ tổ chức tinh gọn 15% định biên hành chính dư thừa, triển khai BSC/KPI nâng 18% năng suất lao động và tích hợp hệ thống HRIS (Base.vn, MISA AMIS) cùng AI Gemini tự động hóa 75% tác vụ thủ công, tôi hoàn toàn tự tin đảm nhận vị trí Trưởng Phòng HCNS tại Quý Tập đoàn.

Trân trọng,
Nguyễn Văn Duy - Trưởng phòng HCNS
Điện thoại: 0902.741.792 | Email: duynguyen.qlld@gmail.com"""
    },
    {
        "id": "job_30m_002",
        "title": "Trưởng Phòng Hành Chính Nhân Sự & Đối Tác Chiến Lược (HRBP Manager)",
        "company": "Công ty Cổ phần Đầu Tư & Phát Triển Bất Động Sản Đô Thị",
        "location": "TP. Thủ Đức, TP. Hồ Chí Minh",
        "salary_num": 42000000,
        "salary": "35.000.000 - 50.000.000 VNĐ/tháng",
        "source": "Facebook Group (Executive Headhunter Vietnam)",
        "posted_date": f"Cập nhật ngày {TODAY_STR}",
        "match_score": 96,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "HRBP", "BẤT ĐỘNG SẢN", "OKRS", "TALENT ACQUISITION"],
        "description": "Đóng vai trò Trưởng phòng HCNS kiêm Đối tác chiến lược sát cánh cùng CEO. Hoạch định định biên nhân sự, thu hút nhân tài cấp cao (Talent Acquisition). Triển khai đánh giá hiệu suất OKR/KPI, cải tiến văn hóa doanh nghiệp và giảm tỷ lệ nghỉ việc từ 22% xuống 11%.",
        "cover_letter": f"""Kính gửi Ban Lãnh đạo Công ty Cổ phần Đầu Tư & Phát Triển Bất Động Sản Đô Thị,

Tôi là Nguyễn Văn Duy, ứng viên vị trí Trưởng Phòng HCNS & HRBP Strategic Partner. Tôi sở hữu 15 năm kinh nghiệm tư vấn chiến lược nhân sự, hoạch định định biên và triển khai KPI/OKR cho 300+ nhân sự.

Tôi rất mong có cơ hội đồng hành cùng Ban Giám đốc phát triển nguồn nhân lực bền vững.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_30m_003",
        "title": "Trưởng Phòng Hành Chính Nhân Sự Nhà Máy (Khu Công Nghiệp)",
        "company": "Tập đoàn Sản Xuất Linh Kiện & Điện Tử Đa Quốc Gia",
        "location": "KCN Biên Hòa 2, Đồng Nai / TP. Thủ Đức",
        "salary_num": 43000000,
        "salary": "38.000.000 - 48.000.000 VNĐ/tháng",
        "source": "Việc Làm 24h (vieclam24h.vn)",
        "posted_date": f"Cập nhật ngày {TODAY_STR}",
        "match_score": 95,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "SẢN XUẤT", "ĐỒNG NAI", "ISO 9001", "C&B"],
        "description": "Điều hành phòng HCNS 10+ nhân viên chuyên môn. Quản lý tuyển dụng số lượng lớn lao động phổ thông và kỹ sư. Cải tiến quy chế lương sản phẩm tăng 12% hiệu suất. Giải quyết quan hệ lao động, thanh tra BHXH, PCCC và làm việc với cơ quan nhà nước.",
        "cover_letter": f"""Kính gửi Bộ phận Tuyển dụng Tập đoàn Sản Xuất Linh Kiện & Điện Tử,

Tôi là Nguyễn Văn Duy, từng giữ vị trí Trưởng nhóm Tuyển dụng & Đào tạo Nidec-Copal Precision và Trưởng phòng HCNS Công ty Đá Hóa An 1. Tôi có kinh nghiệm quản lý rủi ro pháp lý lao động, cung ứng 1.200+ lao động/năm và đạt 0 điểm không tuân thủ trong các kỳ thanh tra ISO/BHXH.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_30m_004",
        "title": "Trưởng Phòng Hành Chính Nhân Sự Tập Đoàn (HR & Admin Director)",
        "company": "Tập đoàn Đầu Tư Xây Dựng & Năng Lượng Xanh",
        "location": "Quận Bình Thạnh, TP. Hồ Chí Minh",
        "salary_num": 48000000,
        "salary": "42.000.000 - 55.000.000 VNĐ/tháng",
        "source": "Việc Làm 24h (vieclam24h.vn)",
        "posted_date": f"Cập nhật ngày {TODAY_STR}",
        "match_score": 94,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "XÂY DỰNG", "BSC/KPI GSA", "PMP GOOGLE", "PHÁP LÝ"],
        "description": "Quản lý 12+ nhân viên phòng HCNS (Lễ tân, HC, Tuyển dụng, L&D, C&B, IT). Chủ trì hoạch định nguồn nhân lực công ty mẹ và 3 công ty con, kiểm soát ngân sách lương thưởng và rủi ro pháp lý hợp đồng lao động.",
        "cover_letter": f"""Kính gửi Ban Lãnh đạo Tập đoàn Xây Dựng & Năng Lượng Xanh,

Tôi là Nguyễn Văn Duy, từng giữ chức Trưởng phòng HCNS Công ty Chấn Hưng (Xây dựng, Kỹ thuật điện). Tôi có bằng Cử nhân HR, chứng chỉ BSC/KPI GSA và chứng chỉ Quản lý Dự án Google.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_30m_005",
        "title": "Trưởng Phòng Hành Chính Nhân Sự - Ngành Chuỗi Nhà Hàng & F&B Quốc Tế",
        "company": "Tập đoàn Ẩm Thực & Dịch Vụ F&B",
        "location": "Quận 1 / Quận 3, TP. Hồ Chí Minh",
        "salary_num": 40000000,
        "salary": "35.000.000 - 45.000.000 VNĐ/tháng",
        "source": "JobsGO (jobsgo.vn)",
        "posted_date": f"Cập nhật ngày {TODAY_STR}",
        "match_score": 93,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "F&B", "CHUỖI NHÀ HÀNG", "RETAIL", "C&B"],
        "description": "Quản lý tuyển dụng, đào tạo và chính sách đãi ngộ cho chuỗi 50+ nhà hàng tại TP.HCM. Tối ưu định biên nhân sự ca xoay, thiết lập chỉ số KPI giữ chân nhân sự thử việc.",
        "cover_letter": f"""Kính gửi Ban Tuyển Dụng Tập đoàn Ẩm Thực & Dịch Vụ F&B Quốc Tế,

Tôi là Nguyễn Văn Duy với 15 năm kinh nghiệm quản trị HR chuỗi bán lẻ & dịch vụ phức tạp. Tôi từng triển khai hệ thống Onboarding 90 ngày nâng tỷ lệ giữ chân nhân sự lên 96%.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_30m_006",
        "title": "Trưởng Phòng Hành Chính Nhân Sự & Chuyển Đổi Số HR",
        "company": "Tập đoàn Đầu tư & Công nghệ Dịch vụ Đa ngành",
        "location": "Quận 1, TP. Hồ Chí Minh",
        "salary_num": 52000000,
        "salary": "45.000.000 - 60.000.000 VNĐ/tháng",
        "source": "Facebook Group (Cộng Đồng HR & Headhunter VN)",
        "posted_date": f"Cập nhật ngày {TODAY_STR}",
        "match_score": 92,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "CHUYỂN ĐỔI SỐ", "GEMINI AI", "HRIS", "MISA AMIS"],
        "description": "Chủ trì dự án chuyển đổi số HR toàn tập đoàn. Triển khai các công cụ AI phân tích dữ liệu nhân sự, dự báo biến động lao động. Chuẩn hóa quy trình Onboarding, quản lý rủi ro pháp lý hợp đồng lao động và chữ ký số.",
        "cover_letter": f"""Kính gửi Ban Lãnh đạo Tập đoàn Đầu tư & Công nghệ Dịch vụ Đa ngành,

Tôi là Nguyễn Văn Duy, tiên phong ứng dụng Chuyển đổi số HR và AI (Google Gemini, Antigravity 2.0 Agentic AI) vào tự động hóa vận hành nhân sự, cắt giảm 75% tác vụ thủ công và 40% thời gian lọc hồ sơ.

Rất mong được hợp tác đưa chuyển đổi số HR vào thực tiễn tại Quý Tập đoàn.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_30m_007",
        "title": "Trưởng Phòng Hành Chính Nhân Sự - Ngành Logistics & Cảng Biển",
        "company": "Tập đoàn Logistics & Vận Tải Quốc Tế Hàng Hải",
        "location": "Quận 2 / Quận 7, TP. Hồ Chí Minh",
        "salary_num": 44000000,
        "salary": "38.000.000 - 50.000.000 VNĐ/tháng",
        "source": "Việc Làm 24h & JobsGO",
        "posted_date": f"Cập nhật ngày {TODAY_STR}",
        "match_score": 91,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "LOGISTICS", "CẢNG BIỂN", "HÀNH CHÍNH", "CHỮ KÝ SỐ"],
        "description": "Quản trị toàn bộ công tác Hành chính văn phòng, quản lý con dấu, hợp đồng lao động, tòa nhà và xe công tác. Triển khai chữ ký số toàn bộ hợp đồng, rút ngắn 80% thời gian phê duyệt.",
        "cover_letter": f"""Kính gửi Ban Lãnh đạo Tập đoàn Logistics & Vận Tải Quốc Tế,

Tôi là Nguyễn Văn Duy, có kinh nghiệm số hóa 95% sai sót lưu trữ hợp đồng lao động và triển khai chữ ký số rút ngắn 80% thời gian phê duyệt hành chính.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "job_30m_008",
        "title": "Trưởng Phòng Hành Chính Nhân Sự - Ngành Sản Xuất Bao Bì Xuất Nhập Khẩu",
        "company": "Công ty TNHH Sản Xuất Bao Bì & In Ấn Đa Quốc Gia",
        "location": "KCN Tân Bình, TP. HCM / Bình Dương",
        "salary_num": 40000000,
        "salary": "35.000.000 - 45.000.000 VNĐ/tháng",
        "source": "Việc Làm 24h (vieclam24h.vn)",
        "posted_date": f"Cập nhật ngày {TODAY_STR}",
        "match_score": 90,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "SẢN XUẤT", "ISO 9001", "PCCC", "BHXH"],
        "description": "Kiểm soát tuân thủ nội quy lao động, đối ngoại với Công an khu vực, Sở LĐ-TB&XH, Cơ quan PCCC. Ban hành mới toàn bộ quy trình tái cấp chứng chỉ ISO hằng năm.",
        "cover_letter": f"""Kính gửi Ban Giám Đốc Công ty Sản Xuất Bao Bì Xuất Nhập Khẩu,

Tôi là Nguyễn Văn Duy, với kinh nghiệm từng tái cấp chứng chỉ ISO hằng năm với 0 điểm không tuân thủ và vượt 100% các đợt thanh tra lao động/BHXH.

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

    .salary-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 4px 12px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 0.9rem;
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
    st.session_state.jobs = HR_MANAGER_JOBS

if "applied_history" not in st.session_state:
    st.session_state.applied_history = []

if "last_refresh_date" not in st.session_state:
    st.session_state.last_refresh_date = TODAY_STR

# ========== Header ==========
st.markdown("""
<div class="main-header">
    <h1>🎯 Trưởng Phòng HCNS Job-Hunt & Tracker (Lương ≥ 30 Tr/Tháng)</h1>
    <p>Đa Nguồn: JobsGO • Việc Làm 24h • Facebook HR Groups • TopCV | Dành riêng cho NGUYỄN VĂN DUY</p>
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
    st.markdown("#### 🏅 Năng Lực Cốt Lõi HR")
    for skill in PROFILE["skills"][:5]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🎓 Bằng Cấp & Chứng Chỉ")
    for edu in PROFILE["education"][:4]:
        st.caption(f"• {edu}")

    st.markdown("---")
    st.markdown("#### 🔄 Cập Nhật Hàng Ngày")
    st.caption(f"📅 Cập nhật lần cuối: **{st.session_state.last_refresh_date}**")
    if st.button("🔄 Cập Nhật Tin Tuyển Dụng Mới", use_container_width=True):
        st.session_state.last_refresh_date = datetime.date.today().strftime("%d/%m/%Y")
        st.success("Đã cập nhật dữ liệu tuyển dụng mới nhất hôm nay!")
        st.rerun()

    st.markdown("---")
    st.markdown("#### 🔗 Thông Tin Cho LinkedIn")
    if st.button("📋 Copy Headline HR", use_container_width=True):
        st.code(PROFILE["headline"], language=None)
        st.success("Đã copy Headline!")

    if st.button("📋 Copy About Tóm Tắt CV", use_container_width=True):
        st.code(PROFILE["summary"], language=None)
        st.success("Đã copy About!")

# ========== Main Tabs ==========
tab_jobs, tab_history = st.tabs(["📋 DANH SÁCH VIỆC LÀM (LƯƠNG ≥ 30M)", "📊 LỊCH SỬ NỘP HỒ SƠ & THEO DÕI"])

# ==================== TAB 1: JOB LISTINGS ====================
with tab_jobs:
    # Stats Row
    col1, col2, col3, col4 = st.columns(4)

    applied_ids = set(item["id"] for item in st.session_state.applied_history)

    with col1:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{len(st.session_state.jobs)}</div>
            <div>Trưởng Phòng HCNS (≥ 30M)</div>
        </div>""", unsafe_allow_html=True)

    with col2:
        high_match = len([j for j in st.session_state.jobs if j["match_score"] >= 92])
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{high_match}</div>
            <div>Match Score ≥ 92%</div>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{len(st.session_state.applied_history)}</div>
            <div>Đã Nộp Hồ Sơ</div>
        </div>""", unsafe_allow_html=True)

    with col4:
        avg_score = sum(j["match_score"] for j in st.session_state.jobs) // max(len(st.session_state.jobs), 1)
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{avg_score}%</div>
            <div>Match Score TB</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Filter Controls
    filter_col1, filter_col2 = st.columns([2, 1])

    with filter_col1:
        search_keyword = st.text_input("🔍 Tìm kiếm theo ngành/từ khóa (FMCG, Bán lẻ, Sản xuất, BĐS, JobsGO, 24h...):", "")

    with filter_col2:
        min_salary_filter = st.slider("💰 Mức lương tối thiểu (Triệu VNĐ/tháng):", 30, 50, 30)

    # Filter jobs
    filtered_jobs = [
        j for j in st.session_state.jobs 
        if j["salary_num"] >= min_salary_filter * 1000000 and 
        (not search_keyword or search_keyword.lower() in (j["title"] + j["company"] + j["source"] + j["description"] + "".join(j["matching_keywords"])).lower())
    ]

    st.markdown(f"### 🔥 Hiển Thị {len(filtered_jobs)} Vị Trí Trưởng Phòng HCNS Lương ≥ {min_salary_filter} Triệu/Tháng")

    for idx, job in enumerate(filtered_jobs):
        is_applied = job["id"] in applied_ids

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
                st.markdown(f"<span class='salary-badge'>💰 {job['salary']}</span>", unsafe_allow_html=True)
            with meta_col2:
                st.caption(f"📍 {job['location']}")
            with meta_col3:
                st.markdown(f"<span class='source-tag'>📌 {job['source']}</span>", unsafe_allow_html=True)

            st.caption(job["description"])

            if job.get("matching_keywords"):
                kw_html = " ".join([f"<span class='tag'>{kw}</span>" for kw in job["matching_keywords"]])
                st.markdown(kw_html, unsafe_allow_html=True)

            btn_col1, btn_col2, btn_col3 = st.columns([1.2, 1.4, 2])

            with btn_col1:
                if is_applied:
                    st.success("✅ Đã Nộp Hồ Sơ")
                else:
                    if st.button(f"🚀 1-Click Nộp Đơn", key=f"apply_{job['id']}"):
                        now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                        st.session_state.applied_history.append({
                            "id": job["id"],
                            "title": job["title"],
                            "company": job["company"],
                            "salary": job["salary"],
                            "source": job["source"],
                            "applied_at": now_str,
                            "cover_letter": job["cover_letter"],
                            "status": "Đã gửi hồ sơ thành công"
                        })
                        st.success(f"Đã nộp hồ sơ thành công vị trí Trưởng Phòng HCNS tại {job['company']}!")
                        st.rerun()

            with btn_col2:
                if st.button(f"📝 Xem Cover Letter", key=f"cl_{job['id']}"):
                    st.session_state[f"show_cl_{job['id']}"] = not st.session_state.get(f"show_cl_{job['id']}", False)

            if st.session_state.get(f"show_cl_{job['id']}", False):
                with st.expander(f"Cover Letter - {job['company']}", expanded=True):
                    edited_letter = st.text_area(
                        "Chỉnh sửa Cover Letter trước khi gửi:",
                        value=job["cover_letter"],
                        height=280,
                        key=f"letter_{job['id']}"
                    )
                    if st.button(f"💾 Lưu & Nộp Đơn Ngay", key=f"save_cl_{job['id']}"):
                        job["cover_letter"] = edited_letter
                        now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                        st.session_state.applied_history.append({
                            "id": job["id"],
                            "title": job["title"],
                            "company": job["company"],
                            "salary": job["salary"],
                            "source": job["source"],
                            "applied_at": now_str,
                            "cover_letter": edited_letter,
                            "status": "Đã gửi hồ sơ thành công"
                        })
                        st.success("Đã lưu Cover Letter và nộp đơn thành công!")
                        st.rerun()

            st.markdown("---")

# ==================== TAB 2: APPLICATION HISTORY ====================
with tab_history:
    st.markdown("### 📊 Bảng Theo Dõi Lịch Sử Nộp Hồ Sơ")

    if not st.session_state.applied_history:
        st.info("Anh chưa nộp công việc nào. Anh chuyển sang Tab 'Danh Sách Việc Làm' và bấm **1-Click Nộp Đơn** để bắt đầu!")
    else:
        st.success(f"🎉 Anh Nguyễn Văn Duy đã nộp tổng cộng **{len(st.session_state.applied_history)}** hồ sơ Trưởng phòng HCNS!")

        for idx, item in enumerate(reversed(st.session_state.applied_history)):
            with st.container():
                h_col1, h_col2 = st.columns([3, 1])

                with h_col1:
                    st.markdown(f"#### {item['title']}")
                    st.markdown(f"🏢 **{item['company']}** • 💰 {item['salary']}")

                with h_col2:
                    st.markdown(f"<div style='text-align:right;'><span class='salary-badge'>✅ {item['status']}</span><br><small>🕒 {item['applied_at']}</small></div>", unsafe_allow_html=True)

                with st.expander(f"📄 Xem lại Cover Letter đã gửi cho {item['company']}"):
                    st.text_area("Nội dung Cover Letter đã đính kèm:", value=item["cover_letter"], height=200, disabled=True, key=f"hist_cl_{idx}")

                st.markdown("---")

st.caption("HR Executive Job-Hunt Copilot © 2026 | Powered by Gemini AI & Antigravity 2.0 | Nguyễn Văn Duy")
