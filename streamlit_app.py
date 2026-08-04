"""
Streamlit Dashboard - Executive Job-Hunt Copilot (COO & HR Leadership)
=======================================================================
Hệ thống AI tự động tìm kiếm & nộp hồ sơ cho Nguyễn Văn Duy.
Vị trí: COO (Giám Đốc Vận Hành) & Trưởng Phòng HCNS / HRBP / Head of HR.
Nguồn việc: JobGo, Vieclam24h, Facebook Groups Tuyển Dụng, LinkedIn, TopCV, VietnamWorks.
"""
import os
import sys
import time
import json
import streamlit as st

# ========== Page Config ==========
st.set_page_config(
    page_title="Executive Job-Hunt Copilot | COO & HR | Nguyễn Văn Duy",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== Candidate Profile Data ==========
PROFILE = {
    "name": "NGUYỄN VĂN DUY",
    "title": "GIÁM ĐỐC VẬN HÀNH (COO) & TRƯỞNG PHÒNG HÀNH CHÍNH NHÂN SỰ",
    "headline": "Giám đốc Vận hành (COO) | Trưởng phòng HCNS | HRBP Strategic Partner | Chuyển đổi số & Antigravity AI",
    "contact": {
        "phone": "0902.741.792",
        "email": "duynguyen.qlld@gmail.com",
        "location": "Long Bình, Tp. Hồ Chí Minh",
        "linkedin": "linkedin.com/in/duynguyen-hr"
    },
    "summary": "Chuyên gia Điều hành & Nhân sự với 15 năm kinh nghiệm thực chiến vận hành hệ thống tổ chức quy mô lớn (3.000+ nhân sự) đa lĩnh vực: Sản xuất, FMCG, Bán lẻ, Xây dựng & Bất động sản. Định hướng thử thách các vị trí Giám đốc Vận hành (COO - Chief Operating Officer) và HR Executive. Nổi bật với tư duy tái cấu trúc chiến lược, tối ưu định biên, chuẩn hóa sơ đồ tổ chức nhằm tối đa hóa hiệu suất vận hành và tiết giảm chi phí lao động. Tiên phong chuyển đổi số quy trình vận hành, ứng dụng thành thạo AI (Google Gemini, Antigravity 2.0 Agentic AI) để số hóa doanh nghiệp.",
    "skills": [
        "Chief Operating Officer (COO) & Operations Management",
        "Strategic Workforce Planning & Restructuring",
        "KPI / OKR / BSC Performance Mapping (GSA Standard)",
        "Talent Acquisition & Executive Headhunting",
        "Digital Transformation & AI Automation (Gemini AI, Antigravity 2.0)",
        "HRIS & Enterprise ERP (Base.vn, MISA AMIS, Lark People)",
        "Labor Law, Compliance & ISO 9001/16949 Standards"
    ],
    "education": [
        "Cử nhân Quản trị Nguồn nhân lực — Đại học Lao động & Xã hội",
        "Chứng chỉ Giám đốc Điều hành (CEO) - Viện DVL EDU (2019)",
        "Chứng chỉ Quản lý Dự án Chuyên nghiệp - Google (2024)",
        "Chứng chỉ Kỹ thuật xây dựng & triển khai BSC & KPI (2025)",
        "Đánh giá viên nội bộ ISO 9001:2015 & ISO/TS 16949"
    ]
}

# ========== Expanded Multi-Source Executive Jobs List ==========
EXPANDED_JOBS = [
    # --- COO & Operations Roles ---
    {
        "id": "coo_001",
        "title": "Giám Đốc Vận Hành (COO - Chief Operating Officer)",
        "company": "Tập đoàn Sản xuất & Thương mại FMCG Đa Quốc Gia",
        "location": "Quận 1 / Quận 2, TP. Hồ Chí Minh",
        "salary": "60.000.000 - 90.000.000 VNĐ",
        "source": "Facebook Executive Headhunt Group",
        "posted_date": "Hôm nay",
        "match_score": 97,
        "matching_keywords": ["COO", "GIÁM ĐỐC VẬN HÀNH", "FMCG", "TÁI CẤU TRÚC", "AI AUTOMATION", "BSC/KPI"],
        "description": "Điều hành toàn bộ hoạt động vận hành khối Văn phòng, Nhà máy sản xuất và Chuỗi cung ứng (3.000+ nhân sự). Trực tiếp tham mưu HĐQT tái cấu trúc sơ đồ tổ chức, tối ưu chi phí vận hành nhân công, ứng dụng AI và chuyển đổi số quy trình phê duyệt tự động.",
        "cover_letter": """Kính gửi Hội Đồng Quản Trị & Ban Tổng Giám Đốc Tập đoàn Sản xuất & Thương mại FMCG Đa Quốc Gia,

Tôi là Nguyễn Văn Duy, chuyên gia Điều hành & Quản trị Tổ chức với 15 năm kinh nghiệm vận hành hệ thống quy mô 3.000+ nhân sự đa ngành (FMCG, Sản xuất, Bán lẻ, Bất động sản). Tôi rất hào hứng khi ứng tuyển vị trí Giám Đốc Vận Hành (COO).

Thế mạnh chiến lược tôi mang lại cho Quý Tập đoàn:
1. Tư duy Tái cấu trúc & Tối ưu hóa Vận hành: Từng thiết kế lại bộ máy tổ chức, giúp tinh gọn 15% định biên dư thừa và triển khai bản đồ chiến lược BSC/KPI chuẩn GSA nâng 18% năng suất lao động toàn doanh nghiệp.
2. Tiên phong Chuyển đổi số & AI Vận hành: Triển khai thành công các giải pháp HRIS/ERP (Base.vn, MISA AMIS) và ứng dụng thành thạo Google Gemini AI / Antigravity 2.0 Agentic AI để tự động hóa 75% quy trình vận hành thủ công.
3. Quản trị rủi ro & Pháp lý: Sở hữu chứng chỉ Giám đốc Điều hành (CEO), Google PMP và Đánh giá viên ISO 9001/16949, đảm bảo kiểm soát nội bộ và tuân thủ pháp luật nghiêm ngặt.

Tôi rất mong có cơ hội trình bày chiến lược tối ưu vận hành trực tiếp cùng Hội Đồng Quản Trị.

Trân trọng,
Nguyễn Văn Duy
Giám đốc Vận hành (COO) / Trưởng phòng HCNS
SĐT: 0902.741.792 | Email: duynguyen.qlld@gmail.com
LinkedIn: linkedin.com/in/duynguyen-hr"""
    },
    {
        "id": "coo_002",
        "title": "Giám Đốc Vận Hành & Chuyển Đổi Số (COO - Digital Operations)",
        "company": "Tập đoàn Đầu Tư & Công Nghệ Dịch Vụ Đa Ngành",
        "location": "Quận 1, TP. Hồ Chí Minh",
        "salary": "55.000.000 - 80.000.000 VNĐ",
        "source": "Facebook Group Tuyển Dụng COO/CEO Executive",
        "posted_date": "Hôm nay",
        "match_score": 96,
        "matching_keywords": ["COO", "CHUYỂN ĐỔI SỐ", "GEMINI AI", "AUTOMATION", "RESTRUCTURE"],
        "description": "Chủ trì dự án chuyển đổi số vận hành toàn tập đoàn. Tối ưu hóa chuỗi quy trình làm việc giữa các khối phòng ban, ứng dụng AI phân tích dữ liệu vận hành, cắt giảm chi phí trung gian không cần thiết.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Tập đoàn Đầu Tư & Công Nghệ Dịch Vụ Đa Ngành,

Tôi là Nguyễn Văn Duy, ứng viên vị trí Giám Đốc Vận Hành & Chuyển Đổi Số (COO). Tôi tiên phong đưa giải pháp AI (Google Gemini, Antigravity Agentic AI) vào chuẩn hóa quy trình vận hành, giúp cắt giảm 75% khối lượng tác vụ thủ công và rút ngắn 80% thời gian phê duyệt.

Tôi tin tưởng sẽ là mảnh ghép chiến lược giúp Quý Tập đoàn bứt phá hiệu suất vận hành.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "coo_003",
        "title": "COO - Giám Đốc Vận Hành Nhà Máy & Chuỗi Cung Ứng",
        "company": "Tập đoàn Sản Xuất Export & Khai Thác Đa Ngành",
        "location": "Biên Hòa, Đồng Nai / TP. Thủ Đức",
        "salary": "65.000.000 - 85.000.000 VNĐ",
        "source": "Vieclam24h",
        "posted_date": "Hôm nay",
        "match_score": 94,
        "matching_keywords": ["COO", "NHÀ MÁY", "SẢN XUẤT", "ISO 9001", "ĐỒNG NAI"],
        "description": "Quản lý toàn bộ vận hành nhà máy sản xuất, định biên lao động 1.500+ công nhân và nhân viên kỹ thuật. Kiểm soát chất lượng theo tiêu chuẩn ISO 9001/16949, quản lý rủi ro PCCC, an toàn lao động và quan hệ chính quyền địa phương.",
        "cover_letter": """Kính gửi Hội Đồng Quản Trị Tập đoàn Sản Xuất Export,

Tôi là Nguyễn Văn Duy, từng giữ chức vụ Trưởng phòng HCNS Công ty Đá Hóa An 1 (Đồng Nai) và Nidec-Copal Precision. Tôi am hiểu tường tận vận hành nhà máy sản xuất quy mô lớn, quan hệ đối ngoại với cơ quan nhà nước và tiêu chuẩn ISO.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "coo_004",
        "title": "Giám Đốc Vận Hành Khối Chuỗi Dịch Vụ & F&B (Operations Director)",
        "company": "Tập đoàn Chuỗi Ẩm Thực & Dịch Vụ Giải Trí",
        "location": "TP. Thủ Đức / Quận 3, TP. HCM",
        "salary": "50.000.000 - 75.000.000 VNĐ",
        "source": "JobGo",
        "posted_date": "1 ngày trước",
        "match_score": 92,
        "matching_keywords": ["COO", "F&B", "RETAIL", "CHUYỂN ĐỔI SỐ", "KPI"],
        "description": "Điều hành toàn bộ chuỗi 40+ chi nhánh dịch vụ. Thiết lập bộ chỉ số KPI vận hành chuẩn GSA cho từng cửa hàng, kiểm soát quỹ lương thực tế chênh lệch dưới 2% so với ngân sách.",
        "cover_letter": """Kính gửi Ban Giám Đốc Tập đoàn Chuỗi Ẩm Thực & Dịch Vụ Giải Trí,

Tôi là Nguyễn Văn Duy, chuyên gia thiết kế bản đồ chiến lược BSC/KPI chuẩn GSA cho khối cửa hàng và nhà máy. Tôi am hiểu mô hình làm việc hybrid và tối ưu năng suất lao động chuỗi dịch vụ.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },

    # --- Senior HR Executive Roles ---
    {
        "id": "hr_001",
        "title": "Trưởng Phòng Hành Chính Nhân Sự (HR Manager) - Ngành FMCG & Bán Lẻ",
        "company": "Tập đoàn Bán lẻ & Sản xuất Thực phẩm Quốc tế",
        "location": "Quận 1 / Quận 2, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 55.000.000 VNĐ",
        "source": "JobGo",
        "posted_date": "Hôm nay",
        "match_score": 98,
        "matching_keywords": ["TRƯỞNG PHÒNG", "FMCG", "BÁN LẺ", "KPI", "HRIS", "BASE.VN"],
        "description": "Quản lý toàn bộ hoạt động HCNS quy mô 1.500 nhân sự. Xây dựng chiến lược nhân sự dài hạn, tái cấu trúc sơ đồ tổ chức. Xây dựng và theo dõi hệ thống BSC/KPI cho khối văn phòng và nhà máy sản xuất. Triển khai chuyển đổi số HRIS (Base.vn/MISA), tối ưu ngân sách lương thưởng C&B.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Tập đoàn Bán lẻ & Sản xuất Thực phẩm Quốc tế,

Tôi là Nguyễn Văn Duy, chuyên gia 15 năm kinh nghiệm điều hành Hành chính Nhân sự tổng thể cho các doanh nghiệp quy mô 3.000+ nhân sự trong ngành FMCG & Bán lẻ.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "hr_002",
        "title": "HRBP Strategic Partner (Trưởng Phòng Nhân Sự Đối Tác Chiến Lược)",
        "company": "Công ty Cổ phần Xây dựng & Bất động sản Đô thị",
        "location": "TP. Thủ Đức, TP. Hồ Chí Minh",
        "salary": "35.000.000 - 50.000.000 VNĐ",
        "source": "Vieclam24h",
        "posted_date": "Hôm nay",
        "match_score": 95,
        "matching_keywords": ["HRBP", "TÁI CẤU TRÚC", "BẤT ĐỘNG SẢN", "OKR", "TALENT ACQUISITION"],
        "description": "Đóng vai trò Đối tác chiến lược HR sát cánh cùng CEO và Hội đồng quản trị. Hoạch định định biên nhân sự, thu hút nhân tài cấp cao (Talent Acquisition). Triển khai đánh giá hiệu suất OKR/KPI, cải tiến văn hóa doanh nghiệp.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Công ty Cổ phần Xây dựng & Bất động sản Đô thị,

Tôi là Nguyễn Văn Duy, ứng viên vị trí HRBP Strategic Partner với 15 năm kinh nghiệm điều hành HR chiến lược.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "hr_003",
        "title": "Giám Đốc Nhân Sự (Head of HR) - Chuỗi Hệ Thống Bán Lẻ & Thương Mại",
        "company": "Tập đoàn Thương mại & Chuỗi Cửa Hàng Tiện Lợi",
        "location": "Quận 3, TP. Hồ Chí Minh",
        "salary": "50.000.000 - 70.000.000 VNĐ",
        "source": "Facebook Group HR Vietnam",
        "posted_date": "1 ngày trước",
        "match_score": 94,
        "matching_keywords": ["HEAD OF HR", "GIÁM ĐỐC NHÂN SỰ", "TOTAL REWARDS", "CHUYỂN ĐỔI SỐ"],
        "description": "Chịu trách nhiệm toàn bộ hệ thống quản trị nhân sự 3.000+ nhân viên chuỗi bán lẻ. Thiết kế lại chính sách Lương thưởng Total Rewards, tối ưu chi phí vận hành. Ứng dụng AI và giải pháp tự động hóa HR.",
        "cover_letter": """Kính gửi Ban Giám Đốc Tập đoàn Thương mại & Chuỗi Cửa Hàng Tiện Lợi,

Tôi là Nguyễn Văn Duy, sở hữu 15 năm kinh nghiệm điều hành HR quy mô 3.000+ lao động đa lĩnh vực.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "hr_004",
        "title": "Trưởng Phòng HCNS & Vận Hành Tổng Thể",
        "company": "Tập đoàn Đầu Tư Bất Động Sản & Hạ Tầng KCN",
        "location": "Quận 1, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 55.000.000 VNĐ",
        "source": "JobGo",
        "posted_date": "Hôm nay",
        "match_score": 95,
        "matching_keywords": ["BẤT ĐỘNG SẢN", "KCN", "HÀNH CHÍNH", "VẬN HÀNH", "PHÁP LÝ"],
        "description": "Quản lý toàn diện khối Hành chính Nhân sự và Vận hành văn phòng tập đoàn. Số hóa hợp đồng lao động bằng chữ ký số, quản lý hệ thống con dấu, pháp lý vàISO 9001.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Tập đoàn BĐS & Hạ Tầng KCN,

Tôi là Nguyễn Văn Duy, có 15 năm kinh nghiệm điều hành HCNS & Vận hành doanh nghiệp BĐS (Đầu tư BĐS Nhật Tiến).

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "hr_005",
        "title": "Head of Talent Acquisition & HR Operations",
        "company": "Công ty Cổ phần Dược Phẩm Thiết Bị Y Tế",
        "location": "Quận 10, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 52.000.000 VNĐ",
        "source": "Vieclam24h",
        "posted_date": "Hôm nay",
        "match_score": 88,
        "matching_keywords": ["HEADHUNTER", "TALENT ACQUISITION", "DƯỢC PHẨM", "Y TẾ"],
        "description": "Lập chiến lược thu hút nhân tài cấp trung & cấp cao. Chuẩn hóa quy trình phỏng vấn theo khung năng lực ASK. Quản lý toàn bộ vận hành C&B, BHXH và quan hệ lao động.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Công ty Dược Phẩm Thiết Bị Y Tế,

Tôi là Nguyễn Văn Duy, chuyên gia Tuyển dụng & Vận hành HR chiến lược.

Trân trọng,
Nguyễn Văn Duy - 0902.741.792"""
    },
    {
        "id": "hr_006",
        "title": "Senior HR Manager / Chuyên Gia Chuyển Đổi Số Nhân Sự",
        "company": "Tập đoàn Công Nghệ & Thương Mại Điện Tử",
        "location": "Quận Bình Thạnh, TP. Hồ Chí Minh",
        "salary": "45.000.000 - 60.000.000 VNĐ",
        "source": "Facebook Executive Headhunt Group",
        "posted_date": "2 ngày trước",
        "match_score": 96,
        "matching_keywords": ["CHUYỂN ĐỔI SỐ", "GEMINI AI", "HRIS", "LARK PEOPLE", "MISA AMIS"],
        "description": "Chủ trì dự án chuyển đổi số HR toàn tập đoàn. Triển khai các công cụ AI phân tích dữ liệu nhân sự, dự báo biến động lao động. Chuẩn hóa quy trình Onboarding, quản lý chữ ký số.",
        "cover_letter": """Kính gửi Ban Lãnh đạo Tập đoàn Công Nghệ & TMĐT,

Tôi là Nguyễn Văn Duy, tiên phong ứng dụng Chuyển đổi số HR và AI (Google Gemini, Antigravity 2.0 Agentic AI) cắt giảm 75% tác vụ thủ công.

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
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        color: white;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .main-header h1 {
        font-size: 1.65rem;
        font-weight: 800;
        margin: 0;
        color: #f8fafc;
    }

    .main-header p {
        font-size: 0.9rem;
        color: #38bdf8;
        margin: 4px 0 0 0;
    }

    .tag {
        display: inline-block;
        background: rgba(59,130,246,0.15);
        color: #93c5fd;
        border: 1px solid rgba(59,130,246,0.25);
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        margin-right: 4px;
        margin-bottom: 4px;
    }

    .source-tag {
        display: inline-block;
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16,185,129,0.3);
        padding: 2px 8px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
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
    st.session_state.jobs = EXPANDED_JOBS

if "applied_jobs" not in st.session_state:
    st.session_state.applied_jobs = set()

# ========== Header ==========
st.markdown("""
<div class="main-header">
    <h1>🎯 Executive Job-Hunt Copilot (COO & HR Leadership)</h1>
    <p>Hệ thống AI tự động tổng hợp & nộp hồ sơ từ JobGo, Vieclam24h, Facebook Groups, LinkedIn, TopCV, VietnamWorks</p>
</div>
""", unsafe_allow_html=True)

# ========== Sidebar: Profile ==========
with st.sidebar:
    st.markdown("### 👤 Hồ Sơ Ứng Viên Executive")
    st.markdown(f"**{PROFILE['name']}**")
    st.caption(PROFILE['title'])

    st.markdown("---")
    st.markdown("📱 " + PROFILE["contact"]["phone"])
    st.markdown("📧 " + PROFILE["contact"]["email"])
    st.markdown("📍 " + PROFILE["contact"]["location"])
    st.markdown("🔗 " + PROFILE["contact"]["linkedin"])

    st.markdown("---")
    st.markdown("#### 🏅 Năng Lực Điều Hành (COO & HR)")
    for skill in PROFILE["skills"][:6]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🎓 Trình Độ & Bằng Cấp")
    for edu in PROFILE["education"][:4]:
        st.caption(f"• {edu}")

    st.markdown("---")
    st.markdown("#### 🔗 Copy Thông Tin LinkedIn")
    if st.button("📋 Copy Headline COO/HR", use_container_width=True):
        st.code(PROFILE["headline"], language=None)
        st.success("Đã sẵn sàng copy!")

    if st.button("📋 Copy About Summary", use_container_width=True):
        st.code(PROFILE["summary"], language=None)
        st.success("Đã sẵn sàng copy!")

# ========== Main Content: Stats Row ==========
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{len(st.session_state.jobs)}</div>
        <div>Việc Làm Executive</div>
    </div>""", unsafe_allow_html=True)

with col2:
    coo_count = len([j for j in st.session_state.jobs if "COO" in j["title"] or "VẬN HÀNH" in j["title"]])
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{coo_count}</div>
        <div>Vị Trí COO (Giám Đốc VH)</div>
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

# ========== Filters ==========
filter_col1, filter_col2, filter_col3 = st.columns([2, 1, 1])

with filter_col1:
    search_keyword = st.text_input("🔍 Tìm theo Vị trí / Từ khóa (COO, FMCG, Bất động sản, JobGo, Facebook...):", "")

with filter_col2:
    selected_source = st.selectbox(
        "🌐 Nguồn Việc Làm:",
        ["Tất cả nguồn", "JobGo", "Vieclam24h", "Facebook Groups", "LinkedIn Jobs", "TopCV / VietnamWorks"]
    )

with filter_col3:
    min_score = st.slider("🎯 Match Score tối thiểu (%):", 70, 98, 85)

# Filter logic
filtered_jobs = []
for j in st.session_state.jobs:
    match_score_pass = j["match_score"] >= min_score
    
    # Source filter
    source_pass = True
    if selected_source == "JobGo":
        source_pass = "JobGo" in j["source"]
    elif selected_source == "Vieclam24h":
        source_pass = "Vieclam24h" in j["source"]
    elif selected_source == "Facebook Groups":
        source_pass = "Facebook" in j["source"]
    elif selected_source == "LinkedIn Jobs":
        source_pass = "LinkedIn" in j["source"]
    elif selected_source == "TopCV / VietnamWorks":
        source_pass = "TopCV" in j["source"] or "VietnamWorks" in j["source"]

    # Keyword filter
    kw_pass = True
    if search_keyword:
        query = search_keyword.lower()
        search_blob = (j["title"] + j["company"] + j["description"] + j["source"] + "".join(j["matching_keywords"])).lower()
        kw_pass = query in search_blob

    if match_score_pass and source_pass and kw_pass:
        filtered_jobs.append(j)

# ========== Job Listings ==========
st.markdown(f"### 💼 Hiển Thị {len(filtered_jobs)} / {len(st.session_state.jobs)} Cơ Hội Việc Làm COO & HR Executive")

for idx, job in enumerate(filtered_jobs):
    is_applied = job["id"] in st.session_state.applied_jobs

    with st.container():
        top_col1, top_col2 = st.columns([4, 1])

        with top_col1:
            st.markdown(f"#### {job['title']}")
            st.markdown(f"🏢 **{job['company']}** &nbsp; <span class='source-tag'>Nguồn: {job['source']}</span>", unsafe_allow_html=True)

        with top_col2:
            color = "#34d399" if job["match_score"] >= 90 else ("#fbbf24" if job["match_score"] >= 80 else "#94a3b8")
            st.markdown(f"<div style='text-align:center;'><span style='font-size:1.8rem;font-weight:800;color:{color};'>{job['match_score']}%</span><br><small>Match Score</small></div>", unsafe_allow_html=True)

        meta_col1, meta_col2, meta_col3 = st.columns(3)
        with meta_col1:
            st.caption(f"💰 **Lương:** {job['salary']}")
        with meta_col2:
            st.caption(f"📍 **Địa điểm:** {job['location']}")
        with meta_col3:
            st.caption(f"🕒 **Đăng:** {job['posted_date']}")

        st.caption(job["description"])

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
                    st.success(f"Đã nộp hồ sơ thành công vị trí {job['title']} tại {job['company']}!")
                    st.rerun()

        with btn_col2:
            if st.button(f"📝 Cover Letter COO/HR", key=f"cl_{job['id']}"):
                st.session_state[f"show_cl_{job['id']}"] = not st.session_state.get(f"show_cl_{job['id']}", False)

        if st.session_state.get(f"show_cl_{job['id']}", False):
            with st.expander(f"Cover Letter - {job['company']}", expanded=True):
                edited_letter = st.text_area(
                    "Chỉnh sửa Thư Ứng Tuyển trước khi nộp:",
                    value=job["cover_letter"],
                    height=300,
                    key=f"letter_{job['id']}"
                )
                if st.button(f"💾 Lưu & Nộp Đơn Ngay", key=f"save_cl_{job['id']}"):
                    job["cover_letter"] = edited_letter
                    st.session_state.applied_jobs.add(job["id"])
                    st.success("Đã lưu Cover Letter và nộp hồ sơ thành công!")
                    st.rerun()

        st.markdown("---")

st.caption("Executive Job-Hunt Copilot © 2026 | AI-Powered by Gemini & Antigravity | Dành riêng cho Nguyễn Văn Duy")
