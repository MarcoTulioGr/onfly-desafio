from helpers import run_cli


def test_le_todas_as_reservas_alem_de_200(tmp_path):
    rows = [{"reservation_id": f"R-{i}"} for i in range(1, 251)] 
    report = run_cli(tmp_path, rows)                                
    assert report["summary"]["total_reservations"] == 250           
    assert report["summary"]["total_amount_brl"] == "25000.00"      

    
def test_virada_de_ano_conta_noites_corretamente(tmp_path):
    rows = [{
        "reservation_id": "R-1",
        "checkin_date": "2024-12-30",
        "checkout_date": "2025-01-02",
    }]
    report = run_cli(tmp_path, rows)
    assert report["summary"]["total_room_nights"] == 3


def test_multiplica_noites_pelo_numero_de_quartos(tmp_path):
    rows = [{
        "reservation_id": "R-1",
        "checkin_date": "2025-01-10",
        "checkout_date": "2025-01-13",
        "rooms": "2",
    }]
    report = run_cli(tmp_path, rows)
    assert report["summary"]["total_room_nights"] == 6