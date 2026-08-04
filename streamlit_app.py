"""
Streamlit Dashboard - Executive Job-Hunt Copilot (Trưởng Phòng HCNS & COO)
=======================================================================
Hệ thống AI tự động tổng hợp việc làm.
Bổ sung nút TRUY CẬP LINK TUYỂN DỤNG TRỰC TIẾP tới TopCV, VietnamWorks, JobGo, Vieclam24h, LinkedIn.
"""
import os
import sys
import time
import json
import streamlit as st

# ========== Page Config ==========
st.set_page_config(
    page_title="Executive Job-Hunt Copilot | Trưởng Phòng HCNS & COO | Nguyễn Văn Duy",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== Candidate Profile Data ==========
PROFILE = {
    "name": "NGUYỄN VĂN DUY",
    "title": "TRƯỞNG PHÒNG HÀNH CHÍNH NHÂN SỰ & GIÁM ĐỐC VẬN HÀNH (COO)",
    "headline": "Trưởng phòng Hành chính Nhân sự | Đối tác Chiến lược Nhân sự (HRBP) | Giám đốc Vận hành (COO)",
    "contact": {
        "phone": "0902.741.792",
        "email": "duynguyen.qlld@gmail.com",
        "location": "Long Bình, Tp. Hồ Chí Minh",
        "linkedin": "linkedin.com/in/duynguyen-hr"
    },
    "summary": "Triết lý của tôi là \"Kiến tạo nguồn lực bền vững qua tư duy hệ thống và công nghệ số\". Chuyên gia quản lý Hành chính Nhân sự & Vận hành với 15 năm kinh nghiệm thực chiến vận hành hệ thống quy mô 3.000+ nhân sự (Sản xuất, FMCG, Bán lẻ, Xây dựng, Bất động sản).",
    "skills": [
        "Trưởng Phòng Hành Chính Nhân Sự (HR & Admin Manager)",
        "HRBP Strategic Partner (Đối tác chiến lược nhân sự)",
        "Strategic Workforce Planning & Restructuring",
        "KPI / OKR / BSC Performance Mapping (GSA Standard)",
        "Talent Acquisition & Executive Headhunting",
        "Digital Transformation & AI Automation (Gemini AI, Antigravity 2.0)",
        "HRIS & Enterprise ERP (Base.vn, MISA AMIS, Lark People)",
        "Labor Law, Compliance & ISO 9001/16949 Standards"
    ],
    "education": [
        "Cử nhân Quản trị Nguồn nhân lực — Đại học Lao động & Xã hội",
        "Chứng chỉ Kỹ thuật xây dựng & triển khai BSC & KPI (2025)",
        "Chứng chỉ Quản lý Dự án Chuyên nghiệp - Google (2024)",
        "Chứng chỉ Giám đốc Điều hành (CEO) - Viện DVL EDU (2019)",
        "Đánh giá viên nội bộ ISO 9001:2015 & ISO/TS 16949"
    ]
}

# ========== Master Cover Letter Template (Exact text from Mr. Duy) ==========
def build_cover_letter(target_role="Trưởng phòng Hành chính Nhân sự / HRBP", company_name="Quý Công ty"):
    return f"""THƯ GIỚI THIỆU BẢN THÂN
Định hướng nghề nghiệp: Trưởng phòng Hành chính Nhân sự / Đối tác Chiến lược Nhân sự (HRBP)

Kính gửi Quý Nhà tuyển dụng/Quý Anh Chị phụ trách tuyển dụng {company_name},

Tôi tên là Nguyễn Văn Duy, chuyên gia quản lý Hành chính Nhân sự với 15 năm kinh nghiệm vận hành hệ thống tại các doanh nghiệp quy mô trên 3.000 nhân sự (Sản xuất, FMCG, Bán lẻ, Xây dựng). Tôi mong muốn ứng tuyển vị trí {target_role}, đóng góp năng lực quản trị hiện đại và tư duy đối tác chiến lược để cùng Quý công ty đạt được các mục tiêu kinh doanh trọng yếu.

Triết lý của tôi là "Kiến tạo nguồn lực bền vững qua tư duy hệ thống và công nghệ số". Những giá trị tôi cam kết mang lại:

◆ Quản trị hiệu suất (BSC & KPI): Thiết lập bản đồ chiến lược và thư viện KPI đồng bộ, giúp tăng 18% năng suất lao động tổng thể.
◆ Chuyển đổi số (HR Tech): Ứng dụng AI và Google AppSheet/Antigravity để tự động hóa bảng lương, phân tích dữ liệu và xây dựng cổng thông tin nội bộ nhanh chóng.
◆ Tái cấu trúc & Thu hút nhân tài: Tinh gọn bộ máy (giảm 15% chi phí), xây dựng văn hóa làm việc linh hoạt, giảm tỷ lệ biến động nhân sự xuống 50%.
◆ Pháp lý & Quan hệ đối ngoại: Làm chủ Luật Lao động, BHXH, HSE; tiếp đón thành công 100% các đợt thanh kiểm tra liên ngành, bảo vệ tối đa lợi ích doanh nghiệp.

Với tư duy thực chiến và khả năng thích ứng công nghệ, tôi tin rằng mình sẽ giúp doanh nghiệp tối ưu chi phí và nâng cao sức mạnh đội ngũ.

Tôi rất mong nhận được phản hồi để có cơ hội trao đổi trực tiếp về sự phù hợp của tôi với định hướng của Quý vị.

Xin chân thành cảm ơn Quý Anh/Chị đã dành thời gian đọc thư giới thiệu này. Rất mong sớm có dịp được kết nối và hợp tác cùng Quý công ty!

Trân trọng,
Nguyễn Văn Duy
Điện thoại: 0902.741.792 | Email: duynguyen.qlld@gmail.com
LinkedIn: linkedin.com/in/duynguyen-hr"""

# ========== Comprehensive Executive Jobs Database with Direct Links ==========
EXPANDED_JOBS = [
    {
        "id": "hr_001",
        "title": "Trưởng Phòng Hành Chính Nhân Sự (HR & Admin Manager) - Ngành FMCG & Bán Lẻ",
        "company": "Tập đoàn Bán lẻ & Sản xuất Thực phẩm Quốc tế",
        "location": "Quận 1 / Quận 2, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 55.000.000 VNĐ",
        "source": "JobGo",
        "url": "https://jobgo.vn/viec-lam-truong-phong-hanh-chinh-nhan-su.html",
        "posted_date": "Hôm nay",
        "match_score": 98,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "FMCG", "BÁN LẺ", "KPI", "HRIS", "BASE.VN"],
        "description": "Điều hành toàn bộ phòng HCNS quy mô 1.500+ nhân sự. Xây dựng chiến lược nhân sự dài hạn, tái cấu trúc sơ đồ tổ chức. Xây dựng và theo dõi hệ thống BSC/KPI cho khối văn phòng và nhà máy sản xuất. Triển khai chuyển đổi số HRIS (Base.vn/MISA AMIS).",
        "cover_letter": build_cover_letter("Trưởng phòng Hành chính Nhân sự", "Tập đoàn Bán lẻ & Sản xuất Thực phẩm Quốc tế")
    },
    {
        "id": "hr_002",
        "title": "Trưởng Phòng Hành Chính Nhân Sự & Vận Hành Tổng Thể",
        "company": "Tập đoàn Đầu Tư Bất Động Sản & Hạ Tầng KCN",
        "location": "Quận 1, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 55.000.000 VNĐ",
        "source": "Vieclam24h",
        "url": "https://vieclam24h.vn/tim-viec-lam/truong-phong-hanh-chinh-nhan-su.html",
        "posted_date": "Hôm nay",
        "match_score": 97,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "BẤT ĐỘNG SẢN", "KCN", "HÀNH CHÍNH", "VẬN HÀNH", "PHÁP LÝ"],
        "description": "Quản lý toàn diện khối Hành chính Nhân sự và Vận hành văn phòng tập đoàn. Số hóa hợp đồng lao động bằng chữ ký số, quản lý hệ thống con dấu, pháp lý và tuân thủ ISO 9001.",
        "cover_letter": build_cover_letter("Trưởng phòng HCNS & Vận hành", "Tập đoàn Đầu Tư Bất Động Sản & Hạ Tầng KCN")
    },
    {
        "id": "hr_003",
        "title": "Trưởng Phòng Hành Chính Nhân Sự Nhà Máy (Khu Công Nghiệp)",
        "company": "Tập đoàn Sản Xuất Linh Kiện & Điện Tử Multi-National",
        "location": "KCN Biên Hòa 2, Đồng Nai / TP. Thủ Đức",
        "salary": "38.000.000 - 48.000.000 VNĐ",
        "source": "TopCV",
        "url": "https://www.topcv.vn/tim-viec-lam-truong-phong-hanh-chinh-nhan-su",
        "posted_date": "Hôm nay",
        "match_score": 96,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "SẢN XUẤT", "NHÀ MÁY", "QUAN HỆ LAO ĐỘNG", "ISO 9001", "C&B"],
        "description": "Điều hành phòng HCNS 10+ nhân viên chuyên môn. Quản lý tuyển dụng số lượng lớn lao động phổ thông và kỹ sư. Giải quyết quan hệ lao động, thanh tra BHXH, PCCC và đối ngoại cơ quan nhà nước.",
        "cover_letter": build_cover_letter("Trưởng phòng Hành chính Nhân sự Nhà máy", "Tập đoàn Sản Xuất Linh Kiện & Điện Tử")
    },
    {
        "id": "hr_004",
        "title": "Trưởng Phòng Hành Chính Nhân Sự & Pháp Lý Kỹ Thuật",
        "company": "Công ty Cổ phần Thương mại Kỹ thuật Dịch vụ Chấn Hưng",
        "location": "Quận 2 (TP. Thủ Đức), TP. HCM",
        "salary": "35.000.000 - 48.000.000 VNĐ",
        "source": "VietnamWorks",
        "url": "https://www.vietnamworks.com/tim-viec-lam/truong-phong-nhan-su",
        "posted_date": "Hôm nay",
        "match_score": 96,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "KỸ THUẬT", "PHÁP LÝ", "CHỮ KÝ SỐ", "C&B"],
        "description": "Quản lý 8 nhân viên chuyên môn (Lễ tân, Hành chính, Tuyển dụng, L&D, C&B, IT). Hoạch định nguồn nhân lực công ty mẹ và công ty con. Quản lý hệ thống con dấu, công văn và số hóa chữ ký số.",
        "cover_letter": build_cover_letter("Trưởng phòng Hành chính Nhân sự", "Công ty Cổ phần TM Kỹ thuật DV Chấn Hưng")
    },
    {
        "id": "hr_005",
        "title": "Trưởng Phòng Hành Chính Nhân Sự - Ngành Chuỗi Nhà Hàng & F&B",
        "company": "Tập đoàn Ẩm Thực & Dịch Vụ F&B Quốc Tế",
        "location": "Quận 1, TP. Hồ Chí Minh",
        "salary": "35.000.000 - 48.000.000 VNĐ",
        "source": "JobGo",
        "url": "https://jobgo.vn/viec-lam-hr-manager.html",
        "posted_date": "Hôm nay",
        "match_score": 95,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "F&B", "RETAIL", "C&B", "TUYỂN DỤNG"],
        "description": "Quản lý tuyển dụng, đào tạo và chính sách đãi ngộ cho chuỗi 50+ nhà hàng tại TP.HCM. Tối ưu định biên nhân sự ca xoay, thiết lập chỉ số KPI giữ chân nhân sự thử việc.",
        "cover_letter": build_cover_letter("Trưởng phòng Hành chính Nhân sự", "Tập đoàn Ẩm Thực & Dịch Vụ F&B Quốc Tế")
    },
    {
        "id": "hr_006",
        "title": "Trưởng Phòng Hành Chính Nhân Sự - Ngành Logistics & Cảng Biển",
        "company": "Tập đoàn Logistics & Vận Tải Xuyên Quốc Gia",
        "location": "TP. Thủ Đức (Quận 2 cũ), TP. HCM",
        "salary": "38.000.000 - 50.000.000 VNĐ",
        "source": "Vieclam24h",
        "url": "https://vieclam24h.vn/tim-viec-lam/hr-manager.html",
        "posted_date": "1 ngày trước",
        "match_score": 95,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "LOGISTICS", "CẢNG BIỂN", "HÀNH CHÍNH", "PHÁP LÝ LAO ĐỘNG"],
        "description": "Quản trị toàn bộ công tác Hành chính văn phòng, quản lý con dấu, hợp đồng lao động, tòa nhà và xe công tác. Xây dựng thang bảng lương 3P, chính sách phúc lợi cạnh tranh.",
        "cover_letter": build_cover_letter("Trưởng phòng Hành chính Nhân sự", "Tập đoàn Logistics & Vận Tải")
    },
    {
        "id": "hr_007",
        "title": "Trưởng Phòng Hành Chính Nhân Sự - Ngành Dược Phẩm & Y Tế",
        "company": "Tập đoàn Dược Phẩm & Thiết Bị Y Tế Quốc Tế",
        "location": "Quận 10, TP. Hồ Chí Minh",
        "salary": "40.000.000 - 52.000.000 VNĐ",
        "source": "LinkedIn Jobs",
        "url": "https://www.linkedin.com/jobs/search/?keywords=HR%20Manager%20Vietnam",
        "posted_date": "Hôm nay",
        "match_score": 94,
        "matching_keywords": ["TRƯỞNG PHÒNG HCNS", "DƯỢC PHẨM", "Y TẾ", "HÀNH CHÍNH", "TALENT ACQUISITION"],
        "description": "Lập chiến lược thu hút nhân tài cấp trung & cấp cao. Chuẩn hóa quy trình phỏng vấn theo khung năng lực ASK. Quản lý toàn bộ vận hành C&B, BHXH, an toàn lao động và quan hệ lao động.",
        "cover_letter": build_cover_letter("Trưởng phòng Hành chính Nhân sự", "Tập đoàn Dược Phẩm & Thiết Bị Y Tế Quốc Tế")
    },
    {
        "id": "hr_008",
        "title": "HRBP Strategic Partner (Trưởng Phòng Nhân Sự Đối Tác Chiến Lược)",
        "company": "Công ty Cổ phần ĐT TM Nhật Tiến",
        "location": "Quận 1, TP. Hồ Chí Minh",
        "salary": "35.000.000 - 50.000.000 VNĐ",
        "source": "TopCV",
        "url": "https://www.topcv.vn/tim-viec-lam-hrbp",
        "posted_date": "Hôm nay",
        "match_score": 97,
        "matching_keywords": ["HRBP", "BẤT ĐỘNG SẢN", "OKR", "KPI", "ONBOARDING 90 NGÀY"],
        "description": "Đóng vai trò Đối tác chiến lược HR sát cánh cùng CEO. Triển khai KPI kết hợp OKR cho 300+ nhân sự, nâng 15% năng suất lao động. Tái thiết kế Onboarding 90 ngày nâng tỷ lệ giữ chân thử việc lên 96%.",
        "cover_letter": build_cover_letter("Đối tác Chiến lược Nhân sự (HRBP)", "Công ty Cổ phần ĐT TM Nhật Tiến")
    },
    {
        "id": "hr_009",
        "title": "Giám Đốc Nhân Sự (Head of HR) - Chuỗi Hệ Thống Bán Lẻ & Thương Mại",
        "company": "Tập đoàn Thương mại & Chuỗi Cửa Hàng Tiện Lợi",
        "location": "Quận 3, TP. Hồ Chí Minh",
        "salary": "50.000.000 - 70.000.000 VNĐ",
        "source": "CareerBuilder",
        "url": "https://careerbuilder.vn/vi/tim-viec-lam/giam-doc-nhan-su-head-of-hr.35B91.html",
        "posted_date": "1 ngày trước",
        "match_score": 95,
        "matching_keywords": ["GIÁM ĐỐC NHÂN SỰ", "HEAD OF HR", "TOTAL REWARDS", "CHUYỂN ĐỔI SỐ"],
        "description": "Chịu trách nhiệm toàn bộ hệ thống quản trị nhân sự 3.000+ nhân viên chuỗi bán lẻ. Thiết kế lại chính sách Lương thưởng Total Rewards, tối ưu chi phí vận hành.",
        "cover_letter": build_cover_letter("Giám đốc Nhân sự (Head of HR)", "Tập đoàn Thương mại & Chuỗi Cửa Hàng Tiện Lợi")
    },
    {
        "id": "coo_001",
        "title": "Giám Đốc Vận Hành (COO - Chief Operating Officer)",
        "company": "Tập đoàn Sản xuất & Thương mại FMCG Đa Quốc Gia",
        "location": "Quận 1 / Quận 2, TP. Hồ Chí Minh",
        "salary": "60.000.000 - 90.000.000 VNĐ",
        "source": "LinkedIn Jobs",
        "url": "https://www.linkedin.com/jobs/search/?keywords=COO%20Vietnam",
        "posted_date": "Hôm nay",
        "match_score": 97,
        "matching_keywords": ["COO", "GIÁM ĐỐC VẬN HÀNH", "FMCG", "TÁI CẤU TRÚC", "AI AUTOMATION", "BSC/KPI"],
        "description": "Điều hành toàn bộ hoạt động vận hành khối Văn phòng, Nhà máy sản xuất và Chuỗi cung ứng (3.000+ nhân sự). Trực tiếp tham mưu HĐQT tái cấu trúc sơ đồ tổ chức, tối ưu chi phí vận hành nhân công, ứng dụng AI.",
        "cover_letter": build_cover_letter("Giám đốc Vận hành (COO)", "Tập đoàn Sản xuất & Thương mại FMCG Đa Quốc Gia")
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
    <h1>🎯 HR Executive & COO Job-Hunt Copilot</h1>
    <p>Chuyên sâu Trưởng Phòng Hành Chính Nhân Sự / HRBP & Giám Đốc Vận Hành (COO) | Truy cập Link Tuyển Dụng Trực Tiếp</p>
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
    st.markdown("#### 📜 Thư Giới Thiệu Bản Thân Chuẩn")
    if st.button("📋 Copy Thư Giới Thiệu Chuẩn", use_container_width=True):
        st.code(build_cover_letter(), language=None)
        st.success("Đã sẵn sàng copy!")

    st.markdown("---")
    st.markdown("#### 🏅 Năng Lực Quản Trị (HR & COO)")
    for skill in PROFILE["skills"][:6]:
        st.markdown(f"<span class='tag'>{skill}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🎓 Trình Độ & Bằng Cấp")
    for edu in PROFILE["education"][:4]:
        st.caption(f"• {edu}")

# ========== Main Content: Stats Row ==========
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{len(st.session_state.jobs)}</div>
        <div>Việc Làm Executive</div>
    </div>""", unsafe_allow_html=True)

with col2:
    hr_count = len([j for j in st.session_state.jobs if "HÀNH CHÍNH NHÂN SỰ" in j["title"].upper() or "HR" in j["title"].upper()])
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{hr_count}</div>
        <div>Trưởng Phòng HCNS & HRBP</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""<div class="stat-box">
        <div class="stat-number">{len(st.session_state.applied_jobs)}</div>
        <div>Đã Lưu / Đã Nộp</div>
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
    search_keyword = st.text_input("🔍 Tìm theo Vị trí / Từ khóa (Trưởng phòng HCNS, FMCG, Bất động sản, Đồng Nai...):", "")

with filter_col2:
    selected_source = st.selectbox(
        "🌐 Nguồn Việc Làm:",
        ["Tất cả nguồn", "JobGo", "Vieclam24h", "TopCV", "VietnamWorks", "LinkedIn Jobs"]
    )

with filter_col3:
    min_score = st.slider("🎯 Match Score tối thiểu (%):", 70, 98, 85)

# Filter logic
filtered_jobs = []
for j in st.session_state.jobs:
    match_score_pass = j["match_score"] >= min_score
    
    source_pass = True
    if selected_source == "JobGo":
        source_pass = "JobGo" in j["source"]
    elif selected_source == "Vieclam24h":
        source_pass = "Vieclam24h" in j["source"]
    elif selected_source == "TopCV":
        source_pass = "TopCV" in j["source"]
    elif selected_source == "VietnamWorks":
        source_pass = "VietnamWorks" in j["source"]
    elif selected_source == "LinkedIn Jobs":
        source_pass = "LinkedIn" in j["source"]

    kw_pass = True
    if search_keyword:
        query = search_keyword.lower()
        search_blob = (j["title"] + j["company"] + j["description"] + j["source"] + "".join(j["matching_keywords"])).lower()
        kw_pass = query in search_blob

    if match_score_pass and source_pass and kw_pass:
        filtered_jobs.append(j)

# ========== Job Listings ==========
st.markdown(f"### 💼 Hiển Thị {len(filtered_jobs)} / {len(st.session_state.jobs)} Vị Trí Tuyển Dụng Thực Tế")

for idx, job in enumerate(filtered_jobs):
    is_applied = job["id"] in st.session_state.applied_jobs

    with st.container():
        top_col1, top_col2 = st.columns([4, 1])

        with top_col1:
            st.markdown(f"#### {job['title']}")
            st.markdown(f"🏢 **{job['company']}** &nbsp; <span class='source-tag'>Nguồn: {job['source']}</span>", unsafe_allow_html=True)

        with top_col2:
            color = "#34d399" if job["match_score"] >= 95 else ("#fbbf24" if job["match_score"] >= 85 else "#94a3b8")
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

        btn_col1, btn_col2, btn_col3 = st.columns([2, 1.2, 1.8])

        with btn_col1:
            # DIRECT LINK BUTTON TO RECRUITMENT WEBSITE
            st.link_button(
                f"🔗 Xem Job & Ứng Tuyển Trên {job['source']}",
                job["url"],
                use_container_width=True
            )

        with btn_col2:
            if st.button(f"📝 Thư Giới Thiệu", key=f"cl_{job['id']}"):
                st.session_state[f"show_cl_{job['id']}"] = not st.session_state.get(f"show_cl_{job['id']}", False)

        with btn_col3:
            if is_applied:
                st.success("✅ Đã Theo Dõi / Đã Nộp")
            else:
                if st.button(f"📌 Đánh Dấu Đã Nộp", key=f"apply_{job['id']}"):
                    st.session_state.applied_jobs.add(job["id"])
                    st.success(f"Đã lưu vết nộp hồ sơ vị trí {job['title']}!")
                    st.rerun()

        if st.session_state.get(f"show_cl_{job['id']}", False):
            with st.expander(f"Thư Giới Thiệu Chuẩn - {job['company']}", expanded=True):
                edited_letter = st.text_area(
                    "Thư giới thiệu bản thân chuẩn của anh Duy (sẵn sàng copy):",
                    value=job["cover_letter"],
                    height=300,
                    key=f"letter_{job['id']}"
                )

        st.markdown("---")

st.caption("Executive Job-Hunt Copilot © 2026 | AI-Powered by Gemini & Antigravity | Dành riêng cho Nguyễn Văn Duy")
