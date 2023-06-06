import streamlit as st

def main():
    # Membuat tampilan navbar
    st.markdown(
        """
        <style>
        .navbar {
            display: flex;
            background-color: #333;
            padding: 10px;
            color: #fff;
            font-family: Arial, sans-serif;
        }

        .navbar a {
            color: #fff;
            text-decoration: none;
            margin-right: 15px;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Menampilkan navbar
    st.markdown(
        """
        <div class="navbar">
            <a href="#">Beranda</a>
            <a href="#">Tentang</a>
            <a href="#">Kontak</a>
        </div>
        """
        , unsafe_allow_html=True
    )

    # Tambahkan konten aplikasi Streamlit Anda di sini
    st.title("Selamat datang di aplikasi Streamlit")

if __name__ == '__main__':
    main()
