@echo off
chcp 65001 >nul
title HR JOB-HUNT COPILOT - NGUYEN VAN DUY
echo.
echo ============================================================
echo   HR EXECUTIVE JOB-HUNT COPILOT
echo   He thong tim viec tu dong cho Nguyen Van Duy
echo ============================================================
echo.
echo Dang khoi dong trang web quan tri...
echo (Trinh duyet se tu dong mo sau vai giay)
echo.

cd /d "d:\tìm việc2026"
py -m streamlit run streamlit_app.py --server.port 8501

echo.
echo Da dong. Bam phim bat ky de thoat...
pause >nul
