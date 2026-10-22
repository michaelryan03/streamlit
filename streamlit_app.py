import streamlit as st

# ==========================================
# 1. CẤU HÌNH TRANG
# ==========================================

st.set_page_config(
    page_title="My Blog - Góc chia sẻ kiến thức",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. DỮ LIỆU BÀI VIẾT MẪU
# ==========================================

articles = [
    {
        "title": "10 xu hướng công nghệ đáng chú ý hiện nay",
        "category": "CÔNG NGHỆ",
        "date": "20/10/2026",
        "description": "Khám phá những xu hướng công nghệ đang thay đổi cách chúng ta làm việc và sinh hoạt.",
        "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800",
        "url": "https://example.com/cong-nghe"
    },
    {
        "title": "Bí quyết xây dựng thói quen đọc sách mỗi ngày",
        "category": "PHÁT TRIỂN BẢN THÂN",
        "date": "19/10/2026",
        "description": "Những phương pháp đơn giản giúp bạn duy trì thói quen đọc sách và học hỏi kiến thức mới.",
        "image": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=800",
        "url": "https://example.com/doc-sach"
    },
    {
        "title": "Kinh nghiệm lên kế hoạch cho chuyến du lịch",
        "category": "DU LỊCH",
        "date": "18/10/2026",
        "description": "Cách chuẩn bị lịch trình, ngân sách và những vật dụng cần thiết cho chuyến đi.",
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800",
        "url": "https://example.com/du-lich"
    },
    {
        "title": "Làm việc hiệu quả với các công cụ trực tuyến",
        "category": "CÔNG NGHỆ",
        "date": "17/10/2026",
        "description": "Tổng hợp các phương pháp tổ chức công việc và quản lý thời gian hiệu quả.",
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800",
        "url": "https://example.com/cong-cu"
    },
    {
        "title": "Những nguyên tắc cơ bản để quản lý chi tiêu",
        "category": "ĐỜI SỐNG",
        "date": "16/10/2026",
        "description": "Tìm hiểu cách theo dõi ngân sách cá nhân và xây dựng kế hoạch chi tiêu hợp lý.",
        "image": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800",
        "url": "https://example.com/chi-tieu"
    },
    {
        "title": "Cách tạo không gian làm việc tối giản",
        "category": "ĐỜI SỐNG",
        "date": "15/10/2026",
        "description": "Sắp xếp góc làm việc gọn gàng để tạo cảm hứng và tập trung tốt hơn.",
        "image": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=800",
        "url": "https://example.com/khong-gian"
    },
]

featured = articles[0]

# ==========================================
# 3. CSS GIAO DIỆN
# ==========================================

st.markdown("""
<style>
    #MainMenu, footer, header {
        visibility: hidden;
    }

    .stApp {
        background-color: #ffffff;
        color: #222222;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }

    .site-logo {
        font-size: 30px;
        font-weight: 800;
        color: #173b35;
        letter-spacing: -1px;
    }

    .site-tagline {
        font-size: 13px;
        color: #777777;
    }

    .section-heading {
        font-size: 25px;
        font-weight: 750;
        color: #173b35;
        margin-top: 26px;
        margin-bottom: 18px;
    }

    .featured-card {
        padding: 20px 0;
    }

    .article-category {
        color: #187b64;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .article-title {
        font-size: 21px;
        font-weight: 750;
        line-height: 1.4;
        margin-bottom: 10px;
        color: #202020;
    }

    .article-description {
        color: #666666;
        font-size: 14px;
        line-height: 1.7;
    }

    .article-meta {
        color: #888888;
        font-size: 12px;
        margin-top: 10px;
    }

    .article-card {
        border: 1px solid #eeeeee;
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 18px;
        height: 100%;
        background: white;
    }

    .article-card img {
        width: 100%;
        height: 170px;
        object-fit: cover;
        border-radius: 7px;
    }

    .sidebar-box {
        padding: 16px;
        background: #f6f8f6;
        border-radius: 10px;
        margin-bottom: 16px;
    }

    .footer-box {
        text-align: center;
        color: #777777;
        font-size: 13px;
        padding: 28px 0;
        border-top: 1px solid #eeeeee;
        margin-top: 35px;
    }

    a {
        text-decoration: none !important;
    }

    @media (max-width: 768px) {
        .site-logo {
            font-size: 25px;
        }

        .section-heading {
            font-size: 22px;
        }

        .article-title {
            font-size: 19px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. HEADER
# ==========================================

header_left, header_right = st.columns([3, 2])

with header_left:
    st.markdown(
        '<div class="site-logo">MY BLOG.</div>'
        '<div class="site-tagline">'
        'Góc chia sẻ kiến thức và trải nghiệm'
        '</div>',
        unsafe_allow_html=True
    )

with header_right:
    search_query = st.text_input(
        "Tìm kiếm bài viết",
        placeholder="Nhập từ khóa...",
        label_visibility="collapsed"
    )

st.divider()

# ==========================================
# 5. MENU ĐIỀU HƯỚNG
# ==========================================

categories = [
    "Tất cả",
    "CÔNG NGHỆ",
    "ĐỜI SỐNG",
    "DU LỊCH",
    "PHÁT TRIỂN BẢN THÂN"
]

selected_category = st.radio(
    "Danh mục",
    categories,
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# ==========================================
# 6. BÀI VIẾT NỔI BẬT
# ==========================================

st.markdown(
    '<div class="section-heading">Bài viết nổi bật</div>',
    unsafe_allow_html=True
)

col_feature, col_sidebar = st.columns([2, 1])

with col_feature:
    st.image(
        featured["image"],
        use_container_width=True
    )

    st.markdown(
        f'<div class="article-category">'
        f'{featured["category"]}</div>'
        f'<div class="article-title">'
        f'{featured["title"]}</div>'
        f'<div class="article-description">'
        f'{featured["description"]}</div>'
        f'<div class="article-meta">'
        f'Ngày đăng: {featured["date"]}</div>',
        unsafe_allow_html=True
    )

    st.link_button(
        "Đọc bài viết →",
        featured["url"]
    )

with col_sidebar:
    st.markdown(
        '<div class="section-heading" '
        'style="margin-top:0">Bài viết mới</div>',
        unsafe_allow_html=True
    )

    for article in articles[1:4]:
        st.markdown(
            f'<div class="sidebar-box">'
            f'<div class="article-category">'
            f'{article["category"]}</div>'
            f'<div style="font-weight:700;line-height:1.5">'
            f'{article["title"]}</div>'
            f'<div class="article-meta">'
            f'{article["date"]}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

# ==========================================
# 7. LỌC VÀ HIỂN THỊ BÀI VIẾT
# ==========================================

st.markdown(
    '<div class="section-heading">Bài viết mới nhất</div>',
    unsafe_allow_html=True
)

filtered_articles = articles

if selected_category != "Tất cả":
    filtered_articles = [
        article for article in filtered_articles
        if article["category"] == selected_category
    ]

if search_query.strip():
    keyword = search_query.strip().casefold()

    filtered_articles = [
        article for article in filtered_articles
        if keyword in article["title"].casefold()
        or keyword in article["description"].casefold()
        or keyword in article["category"].casefold()
    ]

if not filtered_articles:
    st.info("Không tìm thấy bài viết phù hợp.")
else:
    for start in range(0, len(filtered_articles), 3):
        row_articles = filtered_articles[start:start + 3]
        columns = st.columns(3)

        for column, article in zip(columns, row_articles):
            with column:
                st.image(
                    article["image"],
                    use_container_width=True
                )

                st.markdown(
                    f'<div class="article-category">'
                    f'{article["category"]}</div>'
                    f'<div class="article-title">'
                    f'{article["title"]}</div>'
                    f'<div class="article-description">'
                    f'{article["description"]}</div>'
                    f'<div class="article-meta">'
                    f'{article["date"]}</div>',
                    unsafe_allow_html=True
                )

                st.link_button(
                    "Đọc bài viết",
                    article["url"],
                    key=f'link_{start}_{article["title"]}'
                )

                st.write("")

# ==========================================
# 8. FOOTER
# ==========================================

st.markdown("""
<div class="footer-box">
    <strong>MY BLOG.</strong>
    <p>Chia sẻ kiến thức, khám phá điều mới mỗi ngày.</p>
    <p>© 2026 My Blog. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
