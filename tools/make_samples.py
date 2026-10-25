# 시연용 가짜 데이터 생성 (실제 개인정보 없음)
import csv, random, datetime, os, sys

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'samples')
random.seed(7)

def write(name, header, rows):
    with open(os.path.join(out, name), 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)

# 1) 쇼핑몰 주문 내역
items = [('수제 그래놀라 500g', 12900), ('수제 그래놀라 1kg', 22900), ('아몬드 버터 250g', 15800),
         ('오트밀 쿠키 10입', 9800), ('그릭요거트 키트', 18500), ('견과류 믹스 30봉', 27900)]
status = ['배송완료'] * 8 + ['구매확정'] * 6 + ['취소완료', '반품완료']
rows = []
d0 = datetime.datetime(2026, 9, 1, 9)
for i in range(240):
    t = d0 + datetime.timedelta(minutes=random.randint(0, 60 * 24 * 30))
    name, price = random.choice(items)
    q = random.choice([1, 1, 1, 2, 2, 3])
    rows.append([f'2026{t:%m%d}{10000 + i}', t.strftime('%Y-%m-%d %H:%M'), name,
                 random.choice(['', '선물포장', '기본']), q, price, price * q, random.choice(status),
                 f'구매자{i % 97:02d}'])
rows.sort(key=lambda r: r[1])
write('주문내역_9월.csv', ['상품주문번호', '주문일시', '상품명', '옵션정보', '수량', '상품가격',
                         '최종 상품별 총 주문금액', '주문상태', '구매자명'], rows)

# 2) 여러 지점 고객 명단 (서로 겹치는 사람 있음)
people = [(f'고객{i:03d}', f'010-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}') for i in range(120)]
for k, branch in enumerate(['강남점', '홍대점', '잠실점']):
    pick = random.sample(people, 55)
    write(f'고객명단_{branch}.csv', ['이름', '연락처', '최근방문일'],
          [[n, p, f'2026-{random.randint(7, 10):02d}-{random.randint(1, 28):02d}'] for n, p in pick])

# 3) 카드 사용 내역
shops = [('쿠팡', 'online'), ('GS25 역삼점', 'cvs'), ('스타벅스 강남R점', 'cafe'), ('이디야커피', 'cafe'),
         ('카카오T 택시', 'taxi'), ('배달의민족', 'food'), ('쿠팡이츠', 'food'), ('네이버페이 문구', 'online'),
         ('한국전력공사', 'bill'), ('SK텔레콤', 'bill'), ('다이소 강남점', 'store'), ('김밥천국', 'food2')]
rows = []
for i in range(150):
    t = datetime.date(2026, random.randint(7, 9), random.randint(1, 28))
    s, _ = random.choice(shops)
    rows.append([t.isoformat(), s, random.choice([3500, 4800, 6500, 12000, 15900, 23000, 38000, 54000])])
rows.sort()
write('카드내역_7-9월.csv', ['이용일', '가맹점명', '이용금액'], rows)
print('ok', out)
