@echo off
chcp 65001 >nul
title DONG BO LINKEDIN - NGUYEN VAN DUY
echo.
echo ============================================================
echo   HE THONG DONG BO HO SO LINKEDIN TU DONG
echo   Ung vien: NGUYEN VAN DUY - Truong phong HCNS
echo ============================================================
echo.
echo Dang khoi dong trinh duyet Chrome...
echo (Neu lan dau, anh can dang nhap LinkedIn tren cua so Chrome)
echo.

cd /d "d:\tìm việc2026"
py linkedin_updater.py

echo.
echo Da hoan tat. Bam phim bat ky de dong...
pause >nul
