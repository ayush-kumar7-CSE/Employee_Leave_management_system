import main


def test_apply_leave():
    main.employees["E101"]["Casual"] = 12

    main.apply_leave(
        "E101",
        "Casual",
        "2026-11-16",
        "2026-11-18"
    )

    assert main.employees["E101"]["Casual"] == 9


def test_invalid_employee():
    main.apply_leave(
        "E999",
        "Casual",
        "2026-11-16",
        "2026-11-18"
    )


def test_invalid_leave_type():
    main.apply_leave(
        "E101",
        "Other",
        "2026-11-16",
        "2026-11-18"
    )


def test_view_balance():
    main.view_balance("E101")


def test_invalid_date_format():
    main.apply_leave(
        "E101",
        "Casual",
        "16-11-2026",
        "18-11-2026"
    )