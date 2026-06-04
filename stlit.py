import streamlit as st
import pandas as pd
import altair as alt
from streamlit_gsheets import GSheetsConnection
import datetime

# 페이지 설정
st.set_page_config(page_title="나의 관심사", page_icon="✨", layout="wide")

# 메인 타이틀
st.markdown("<div id='intro'></div>", unsafe_allow_html=True)
st.title("저의 관심사를 소개합니다! 🎉")
st.write("제가 좋아하는 것들과 취미를 공유해보려 합니다. 아래에서 저의 다양한 관심사를 확인해보세요!")

st.divider()

st.markdown("<h1 style='font-size: 45px; margin-bottom: 20px;'>📝 간단 요약</h1>", unsafe_allow_html=True)

# 레이아웃을 3개의 컬럼으로 나누어 관심사 병렬 표현
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div id='football'></div>", unsafe_allow_html=True)
    st.header("1. 축구 ⚽")
    st.write("축구 보는 것을 매우 좋아합니다. 특히 EPL에 토트넘이라는 팀을 열렬히 응원하고 있습니다..")
    st.info("두 시즌 연속 17등이라도 좋습니다...")

with col2:
    st.markdown("<div id='music'></div>", unsafe_allow_html=True)
    st.header("2. 음악 감상 🎵")
    st.write("생각이 많아질때나 힘들때 음악을 많이 듣습니다. 평범한 순간도 음악과 함께면 특별해지는 것 같습니다.")
    st.success("요즘 즐겨 듣는 장르: 힙합, 인디")

with col3:
    st.markdown("<div id='reading'></div>", unsafe_allow_html=True)
    st.header("3. 독서 📚")
    st.write("사실 책 읽는 것을 그다지 좋아하지 않습니다. 그래도 추천하고 싶은 책이 조금 있어서 해봅니다.")
    st.success("최근 관심 분야: 인문학, 과학")

st.divider()

st.markdown("<h1 id='본격적인-설명-들어갑니다' style='font-size: 45px; margin-bottom: 20px;'>🔍 본격적인 설명 들어갑니다.</h1>", unsafe_allow_html=True)

# 탭(버튼) 크기를 키우기 위한 CSS 디자인 적용
st.markdown("""
<style>
    div[data-testid="stTabs"] button {
        font-size: 22px !important;
        font-weight: bold !important;
        padding: 15px 30px !important;
    }
</style>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["⚽ 축구", "🎵 음악", "📚 독서"])

with tab1:
    st.subheader("우리 토트넘 빅6 맞습니다. 토트넘을 사랑하는 이유")
    st.write("일단 토트넘이 어떤 팀인지 알아보시죠. 사랑하지 않을 수 없습니다. ")
    
    # 토트넘 로고 이미지
    st.markdown('<img src="https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg" width="150" style="margin-bottom: 20px;">', unsafe_allow_html=True)
    
    # 토트넘 역사 간단 설명
    st.markdown("""
    **토트넘 홋스퍼 FC (Tottenham Hotspur FC)**는 1882년에 창단된 잉글랜드 런던 북부를 연고로 하는 유서 깊은 클럽입니다. 
    수비보다는 공격을 중시하는 'To Dare Is To Do(실천이 곧 도전이다)'라는 멋진 모토를 가지고 있죠. 
    최근 우승 트로피와는 인연이 닿지 않아 팬들의 애간장을 녹이고 있지만, 언제나 화끈하고 재미있는 경기를 보여주는 매력적인 팀입니다!
    """)
    
    # 최근 리그 순위 막대 그래프 (이번 시즌 포함 5시즌)
    st.write("**📈 최근 5시즌 프리미어리그 순위**")
    
    # 시즌이 가로(x축)로 가도록 데이터 프레임 구성
    rankings_data = pd.DataFrame({
        '시즌': ['21/22', '22/23', '23/24', '24/25', '25/26(현재)'],
        '순위': [4, 8, 5, 17, 17]  # 25/26 시즌의 임시 순위 (희망사항 반영!)
    })
    
    # Altair를 사용하여 순위가 높을수록(숫자가 작을수록) 위로 가도록 직관적인 막대 그래프 생성
    bars = alt.Chart(rankings_data).mark_bar(color='#132257').encode(
        x=alt.X('시즌:N', title='시즌', sort=None, axis=alt.Axis(labelAngle=0)),
        # 세로축(y축, 가로선) 숫자를 1단위로 표시하기 위해 values 지정
        y=alt.Y('순위:Q', scale=alt.Scale(domain=[20, 1], reverse=True), 
                axis=alt.Axis(values=list(range(1, 21))), title='리그 순위'),
        tooltip=['시즌', '순위']
    )
    
    # 직관성을 높이기 위해 막대 안/위에 순위 숫자 표시
    text = bars.mark_text(
        align='center',
        baseline='middle',
        dy=15,  # 텍스트를 막대 안쪽으로 약간 내림
        color='white',
        fontWeight='bold'
    ).encode(
        text='순위:Q'
    )
    
    chart = (bars + text).properties(height=350)
    
    st.altair_chart(chart, use_container_width=True)
    
    # 최근 3시즌 실적 요약 추가
    st.markdown("""
    ---
    ### 🎢 토트넘의 최근 행보: 말 그대로 '극과 극'
    리그에서는 턱밑까지 강등 위기가 찾아와 지옥을 맛봤는데, 유럽 대회에서는 기적 같은 성과를 내며 천국을 오갔습니다.
    
    #### 🏴󠁧󠁢󠁥󠁮󠁧󠁿 최근 프리미어리그(EPL) 실적
    국내 리그에서는 강등권 언저리를 맴돌며 구단 역사상 가장 아슬아슬한 시기를 보냈습니다.
    * **2023-2024 시즌: 5위 (승점 66점)**
      엔제 포스테코글루 감독의 데뷔 시즌이자 손흥민 선수가 주장을 맡았던 해입니다. 초반 상승세를 타며 최종 5위로 마감했고, 유로파리그 진출권을 따냈습니다.
    * **2024-2025 시즌: 17위 (승점 38점)**
      팀이 통째로 흔들리며 48년 만의 최저 순위인 17위로 추락했습니다. 구단 역사상 최저 승점(38점)으로 강등 직전까지 몰렸으나, 아래 팀들이 무너진 덕분에 간신히 잔류했습니다.
    * **2025-2026 시즌: 17위 (승점 41점)**
      방금 막 끝난 이번 시즌에도 고전은 이어졌습니다. 18위 웨스트햄을 단 2점 차로 제치고 정말 턱걸이로 잔류에 성공했습니다.
      
    #### 🌍 최근 유럽 대항전 실적
    리그에서의 처참한 부진과 달리, 유럽 무대에서는 전 세계 축구 팬들을 놀라게 한 반전 드라마를 썼습니다.
    * **2023-2024 시즌: 진출 실패**
      전전 시즌 8위에 그친 여파로 유럽 대항전에 진출하지 못했습니다.
    * **2024-2025 시즌: UEFA 유로파리그 우승 🏆**
      토트넘 역사에 남을 역대급 시즌입니다. 리그에서는 강등을 걱정하던 팀이 유로파리그 결승에서 맨유를 1-0으로 꺾고 41년 만에 유럽 대회 우승을 차지했습니다! 덕분에 다음 시즌 챔스 직행권까지 따냈습니다.
    * **2025-2026 시즌: UEFA 챔피언스리그 16강**
      본선에서 도르트문트, 프랑크푸르트 등을 제치고 토너먼트에 올랐지만, 16강전에서 아틀레티코 마드리드에 합산 스코어 5-7로 패하며 아쉽게 여정을 마무리했습니다.
    """)
    
    # 우리가 사랑하던 토트넘 (과거 황금기)
    st.markdown("""
    ---
    ### <img src="https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg" width="35" style="vertical-align: middle; margin-bottom: 5px; margin-right: 5px;"> 우리가 사랑하던 토트넘
    지금의 힘겨운 잔류 싸움을 생각하면 눈물이 앞을 가릴 정도로, 불과 몇 년 전 마우리시오 포체티노 감독 시절의 토트넘은 프리미어리그를 넘어 유럽 전체가 두려워하던 엄청난 강팀이었습니다. 토트넘 역사상 최고의 황금기라 불리는 시절의 기록입니다.
    
    #### 1. 구단 역사상 최다 승점, 리그 2위 (2016-17 시즌)
    이때의 토트넘은 공수 밸런스가 리그 완벽 탑티어였습니다. 첼시가 미친 연승 행진을 달리는 바람에 아쉽게 우승은 놓쳤지만, 경기력은 우승팀 못지않았습니다.
    * **승점 86점 (구단 역사상 EPL 최다 승점)**: 26승 8무 4패를 기록하며 당당히 2위에 올랐습니다. 리그 최다 득점(86골)과 최소 실점(26골)을 동시에 기록한 완벽한 시즌이었습니다.
    * **홈구장 '화이트 하트 레인'의 유종의 미**: 118년 동안 쓴 홈구장을 허물고 새 구장을 짓기 전 마지막 시즌, 홈에서 17승 2무(무패)라는 경이로운 성적을 거두며 최고의 선물을 안겼습니다.
    * **통곡의 벽 'DESK + 베르통언·알더베이럴트'**: 공격진뿐만 아니라 벨기에 듀오가 버틴 수비와 요리스 골키퍼까지 완벽해서 그야말로 '숨 막히는 축구'를 구사했습니다.
    
    #### 2. 기적과 눈물의 챔피언스리그 준우승 (2018-19 시즌)
    이 시즌은 팬들에게 평생 잊지 못할 '기적의 드라마' 그 자체였습니다. 이적 시장에서 '0입'을 기록했는데도 기존 스쿼드의 잇몸과 정신력으로 결승까지 진격했거든요.
    * **8강 맨시티전 (손흥민의 하드캐리)**: 우승 후보 0순위였던 맨시티를 만나 손흥민 선수가 1, 2차전 합쳐 3골을 폭발시키며 팀을 4강으로 이끌었습니다.
    * **4강 아약스전 (암스테르담의 기적)**: 2차전 후반까지 합산 스코어 0-3으로 뒤지다 루카스 모우라의 후반 추가시간 버저비터 포함 해트트릭으로 극적인 결승 진출을 이뤘습니다.
    * **마드리드에서의 결승전**: 리버풀과의 결승에서 시작 2분 만에 아쉬운 페널티킥 선제골을 내주며 0-2로 준우승에 머물렀지만, 토트넘 역사상 최초의 UCL 결승 진출이라는 위대한 이정표를 세웠습니다.
    
    <div style="display: flex; align-items: center; gap: 20px; margin-top: 10px; margin-bottom: 20px;">
        <img src="https://preview.redd.it/just-one-tottenham-player-remains-from-spurs-2019-champions-v0-vou7x6z6g99c1.jpeg?auto=webp&s=b4083fbb9bbd5936eeee8d6bb5de482551f3f974" width="60%" style="border-radius: 10px;">
        <p style="font-size: 0.95em; color: #666; line-height: 1.5; margin: 0;">
            💡 <strong>사진 부연 설명:</strong><br>
            이 2018-19 챔피언스리그 결승전 스쿼드 중, <strong>24/25 시즌 기준</strong> 현재까지 토트넘에 남아있는 선수는 오직 주장 <strong>'손흥민'</strong> 단 한 명뿐입니다.
        </p>
    </div>
    
    #### 3. 유럽을 공포에 떨게 한 오각 편대의 핵, 'DESK' 라인
    당시 토트넘의 화력을 책임졌던 네 명의 공격진, **D**ele, **E**riksen, **S**on, **K**ane! 유럽에서 가장 파괴력 있고 유기적인 조합이었고 라커룸에서도 엄청난 절친들이었죠.
    * **D - 델레 알리 (Dele Alli)**: 천재적인 오프더볼 능력을 갖춘 섀도우 스트라이커! 케인이 공간을 만들면 귀신같이 찾아 들어가 골을 넣던, '보얀이나 메시급 유망주' 찬사를 받던 선수였습니다.
    * **E - 크리스티안 에릭센 (Christian Eriksen)**: 팀의 '두뇌'이자 축구 도사! 지치지 않는 체력과 자로 잰 듯한 패스로 찬스를 만들던 대체 불가능한 사령관이었습니다.
    * **S - 손흥민 (Son Heung-min)**: 스피드와 양발 슈팅력을 무기로 한 최고의 피니셔! 폭발적인 속도로 뒷공간을 허물고, 케인과 EPL 역사상 최다 합작골(47골)을 기록한 전설입니다.
    * **K - 해리 케인 (Harry Kane)**: 세계 최고의 '육각형 공격수'! 골뿐만 아니라 미드필더 지역까지 내려와 플레이메이킹을 주도하며 토트넘 전술의 시작이자 끝이었습니다.
    
    이 네 선수가 유기적으로 스위칭하며 에릭센이 찌르고, 케인이 버티고, 알리가 휘젓고, 손흥민이 마무리하던 시절의 토트넘은 그야말로 '낭만 축구'의 정점이었습니다. 지금의 토트넘을 보면 이때가 더 그리워지곤 하네요.
    
    <img src="https://pbs.twimg.com/media/DwasWS8XgAI7OXg.jpg" width="70%" style="border-radius: 10px; margin-top: 10px;">
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # 영원한 캡틴 손흥민
    st.markdown("""
    ### 👑 영원한 캡틴 손흥민
    #### 1. 전성기 시절: 'DESK' 라인의 폭발과 유럽을 흔든 진격
    2015년 토트넘의 유니폼을 입은 손흥민은 마우리시오 포체티노 감독 아래서 무서운 속도로 성장했습니다. 이 시절 손흥민은 해리 케인, 델레 알리, 크리스티안 에릭센과 함께 이른바 'DESK 라인'을 구축하며 프리미어리그 최고의 화력을 자랑했습니다.
    * **2016-17 시즌 리그 2위**: 구단 역사상 프리미어리그 최다 승점(86점)을 기록하며 전성기의 서막을 알렸습니다.
    * **2018-19 시즌 챔피언스리그 결승 진출**: 해리 케인이 부상으로 쓰러진 절체절명의 순간, 손흥민은 맨시티와의 8강전에서 홀로 3골을 터트리는 등 팀을 사상 최초의 UCL 결승으로 견인하며 '월드클래스'의 반열에 당당히 올라섰습니다.

    #### 2. 득점왕(Golden Boot): 아시아 축구 역사를 새로 쓰다 (2021-22)
    손흥민의 개인 커리어에서 가장 눈부시게 빛나는 순간은 단연 2021-22 시즌 프리미어리그 득점왕 등극입니다.
    시즌 막판 엄청난 몰아치기로 리그 23골을 터트리며 모하메드 살라와 함께 공동 득점왕(골든 부트)을 차지했습니다. 특히 이 23골 중 페널티킥(PK)이 단 한 개도 없었다는 점에서 전 세계 축구계를 경악하게 만들었습니다. 아시아인 최초의 EPL 득점왕이라는 이 위대한 업적은 손흥민이라는 이름 석 자를 프리미어리그 역사에 영원히 각인시켰습니다.
    """)
    
    st.image("golden_boot.jpg", use_container_width=True)
    
    st.markdown("""
    #### 3. 유로파리그 우승: 17년의 한을 푼 '캡틴'의 마지막 춤 (2024-25)
    수많은 이적 제안을 거절하고 끝까지 토트넘에 남은 손흥민에게 가장 결핍되어 있던 것은 다름 아닌 '우승 트로피'였습니다. 그리고 그 한은 2024-25 시즌, 가장 극적인 방식으로 풀리게 됩니다.
    당시 토트넘은 리그에서 17위까지 추락하며 창단 이래 최대의 위기를 겪고 있었습니다. 주장이었던 손흥민은 무너져가는 팀의 중심을 잡고 유로파리그(UEL) 무대에 모든 것을 쏟아부었습니다.
    마침내 2025년 5월 빌바오에서 열린 맨체스터 유나이티드와의 결승전에서 1-0 승리를 거두며, 토트넘의 17년 무관 징크스를 깨부수고 주장으로서 당당히 우승 트로피를 들어 올렸습니다. 가장 힘겨운 시즌에 이뤄낸 기적 같은 우승이었습니다.

    #### 📝 아름다운 마침표: 토트넘 커리어의 대단원
    **"우승 트로피를 들고 떠나는 전설"**
    
    손흥민은 이 유로파리그 우승을 끝으로 토트넘에서의 찬란했던 커리어를 완벽하게 마무리했습니다.
    팀이 가장 힘들 때 맹목적인 로열티(충성심)로 헌신했고, 구단과 팬들이 그토록 염원하던 유럽 대항전 트로피를 선물한 뒤 박수칠 때 떠나는 최고의 엔딩을 선택한 것입니다.
    비록 붙박이 빅클럽은 아니었을지라도, 한 팀의 리더로서 지옥과 천국을 모두 경험하며 마침내 정상에서 마침표를 찍은 그의 서사는 축구 역사상 가장 아름답고 낭만적인 '원클럽맨급 전설'의 스토리로 영원히 기억될 것입니다.
    """)
    
    st.image("son_trophy.jpg", use_container_width=True)
    
    st.divider()
    

with tab2:
    st.subheader("노래없이는못살겠어요. 에어팟 닳게 만드는 노래")
    st.write("이제부터는 지극히 개인적으로 좋아하는 노래들을 설명하려고 합니다. 꼭 한번씩 들어보시길 바랍니다!!")
    
    st.divider()
    
    st.markdown("### 🔁 최근 무한반복 중인 플레이리스트")
    st.markdown("요즘 가장 많이 듣고 있는 곡들입니다.")
    
    col_text, col_img1, col_img2, col_img3 = st.columns([6, 1.2, 1.2, 1.2])
    
    with col_text:
        st.info("💡 **최근 나의 BGM:** 요즘 길을 걸을 때나 쉴 때 가장 많이 듣는 노래 3곡입니다")
        st.markdown("""
        <div style='margin-top: -10px; margin-bottom: -10px;'>
        1. **포커페이스 - C JAMM**: 기본적으로 노래 자체의 분위기가 너무 좋고, 씨잼 특유의 반항적인 느낌에 완전히 빠져버렸습니다. 모두가 맞다는 말에 아니라고 할 수 있는 멋을 느낄 수 있습니다.<br>
        2. **It's You  - 한요한,NO:EL**: 기타 베이스의 멜로디랑 공감되는 가사가 정말 좋습니다. 한요한의 거친 목소리도 좋은데, 이 노래는 노엘 씹어먹은 노래라고해도 과언이 아닙니다. 노엘의 긁는 듯한 목소리랑 플로우가 예술입니다.<br>
        3. **20 Min- Lil Uzi Vert**: 이 노래는 뭔가 몽환적인 듯하면서도 중독전인 멜로디가 매력적인 노래입니다. 사운드 자체도 편하게 듣기 좋고, 자연스럽게 고개를 끄덕이게 됩니다. 
        </div>
        """, unsafe_allow_html=True)
        
    with col_img1:
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        st.image("bgm_1.jpg", use_container_width=True, caption="포커페이스")
    with col_img2:
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        st.image("bgm_2.jpg", use_container_width=True, caption="It's You")
    with col_img3:
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        st.image("bgm_3.jpg", use_container_width=True, caption="20 Min")
    
    st.divider()
    
    st.markdown("### 🎤 가장 좋아하는 아티스트")
    st.markdown("#### 로꼬")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("loco.webp", use_container_width=True)
    with col2:
        st.markdown("제가 개인적으로 가장 좋아하는 래퍼입니다. 로꼬(Loco)는 대한민국 대표 힙합 서바이벌 <쇼미더머니> 시즌 1의 초대 우승자로, 대중성과 음악성을 모두 잡은 힙합 신의 대표적인 '믿고 듣는 음원 강자'입니다. 귀에 쏙쏙 박히는 정확한 발음의 래핑과 특유의 밝고 편안한 멜로디로 남녀노소 누구나 즐길 수 있는 이지리스닝 힙합을 구사하는 것이 특징입니다. 저의 재수 생활에 가장 큰 힘이 됐던 아티스트이고 관련된 추억도 많습니다.")
    
    st.markdown("**🎶 나의 최애곡 3선**")
    
    song1_col1, song1_col2 = st.columns([1, 4])
    with song1_col1:
        st.image("loco_1.jpg", use_container_width=True)
    with song1_col2:
        st.markdown("**1. 시간이 들겠지**\n\n재수 생활때 매일을 똑같이 살아가면서 지나간 시간에 대한 기억은 잊고 만족스럽지 못한 결과만 남았을 때, 이 노래의 가사가 많이 와닿더라고요. 수능 끝나고 재수학원 바닥에 누워서 하늘을 바라보면서 이 노래를 들었던 기억이 납니다 ㅎ.. 제가 있던 학원이 기숙학원이였는데 수능 끝나고서 대부분이 바로 집을 가고 몇명만 남았다가 다음날에 가게됩니다. 그래서 사람이 바글거리던 그 큰 학원에 아무도 없는 모습을 보는데 생각이 많아지더라고요.  ")
        
    song2_col1, song2_col2 = st.columns([1, 4])
    with song2_col1:
        st.image("loco_2.jpg", use_container_width=True)
    with song2_col2:
        st.markdown("**2. 니가 모르게**\n\n짝사랑을 해본사람이라면 누구나 공감할만한 가사가 아주 매력적입니다. 멜로디 자체도 정말 듣기 좋아서 많이 듣는 노래입니다.")
        
    song3_col1, song3_col2 = st.columns([1, 4])
    with song3_col1:
        st.image("loco_3.jpg", use_container_width=True)
    with song3_col2:
        st.markdown("**3. 감아**\n\n이 노래도 재수 생활을 할 때, 많은 위로를 받았던 노래입니다. 가사 또한 아주 훌륭합니다.")
        
    st.write("") # 여백
    
    st.markdown("#### Post Malone")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("postmalone.png", use_container_width=True)
    with col2:
        st.markdown("포스트 말론은 외국 힙합을 입문하게 해준 아티스트입니다. 저의 외힙 취향을 만들어줬다고 볼 수 있을 것 같습니다. 포스트 말론(Post Malone)은 힙합, 록, 팝, 알앤비 등 장르의 경계를 완벽하게 허물며 전 세계 빌보드 차트를 장악한 글로벌 슈퍼스타입니다. 특유의 거칠고 호소력 짙은 허스키 보이스와 귀에 꽂히는 중독성 있는 멜로디 라인이 무기이며, 최근에는 컨트리 음악 장르까지 섭렵하며 폭넓은 스펙트럼을 보여주고 있습니다. 거구의 몸과 얼굴 타투라는 강렬한 외모와 달리, 무대 밖에서는 지독할 정도로 순박하고 친근한 반전 매력으로 국내외에서 엄청난 사랑을 받고 있습니다.")
    
    st.markdown("**🎶 나의 최애곡 3선**")
    
    song1_col1, song1_col2 = st.columns([1, 4])
    with song1_col1:
        st.image("post_1.jpg", use_container_width=True)
    with song1_col2:
        st.markdown("**1. Goodbyes**\n\n노래의 시작 부분이 무거운 것 같지만 비트의 분위기 약간 바뀌면서 노래에 몰입하게 됩니다. 그리고 이 노래 자체의 멜로디가 말이 안되게 좋고, 피처링도 정말 좋습니다. 처음에 이 노래를 들었을 때의 전율을 잊을 수 없습니다.")
        
    song2_col1, song2_col2 = st.columns([1, 4])
    with song2_col1:
        st.image("post_2.jpg", use_container_width=True)
    with song2_col2:
        st.markdown("**2. congratulation**\n\n처음 들으면 '와 진짜 힙하다' 라는 느낌을 자연스럽게 받을 수 있는 노래입니다. 어느새 고개를 끄덕이고 있는 자신을 볼 수 있을 겁니다.")
        
    song3_col1, song3_col2 = st.columns([1, 4])
    with song3_col1:
        st.image("post_3.jpg", use_container_width=True)
    with song3_col2:
        st.markdown("**3. circles**\n\n이 노래로 포스트 말론을 처음 접하게 된걸로 기억합니다. 당시 중학교때 페이스북에서 이 노래를 처음 들었던 것 같은데, 그때는 이런 느낌의 노래를 처음 들어봐서 충격 받았던 기억이 납니다.")
        
    st.write("") # 여백
    
    st.markdown("#### 빈지노")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("beenzino.jpg", use_container_width=True)
    with col2:
        st.markdown("빈지노(Beenzino)는 한국 힙합 역사에서 결코 빼놓을 수 없는 독보적인 아이콘이자, 음악을 넘어 패션과 시각 예술까지 아우르는 아티스트들의 아티스트입니다. 세련된 플로우와 마치 한 편의 영화나 에세이를 보는 듯한 감각적인 가사 스타일로 한국 힙합의 세대교체를 이끌었습니다. 평단과 대중의 극찬을 받으며 한국대중음악상을 휩쓴 정규 앨범 'NOWITZKI(노비츠키)' 이후, 최근에는 오랜 팬들이 손꼽아 기다려온 그룹 '재지팩트(Jazzyfact)'의 새 앨범 작업을 준비 중이라는 반가운 소식을 전하며 여전한 영향력을 증명하고 있습니다.")
    
    st.markdown("**🎶 나의 최애곡 3선**")
    
    song1_col1, song1_col2 = st.columns([1, 4])
    with song1_col1:
        st.image("beenzino_1.jpg", use_container_width=True)
    with song1_col2:
        st.markdown("**1. Always Awake**\n\n젊음이라는 추상적인 느낌을 현실적인 삶으로 풀어내는 느낌이 매우 인상적이였습니다. 그리고 열정적으로 살아가는 삶의 멋을 느낄 수 있었습니다. 시험기간에 새벽 공부를 마치고 집가는 길에 후드를 뒤집어쓰고 들으면 노래의 느낌을 훨씬 잘 살릴 수 있습니다 ㅎㅎ.. 저도 시험기간만 되면 매번 찾게 되는 노래입니다. ")
        
    song2_col1, song2_col2 = st.columns([1, 4])
    with song2_col1:
        st.image("beenzino_2.jpg", use_container_width=True)
    with song2_col2:
        st.markdown("**2. Smoking dreams**\n\n고민이 많아지는 순간마다 찾게 되는 노래 같네요. 방황하고 고민하는 사람이라면 누구나 공감하며 들을 것 같습니다. 위에 노래처럼 시험기간에 많이 듣는 노래고 가끔 '이렇게 사는게 맞을까?' 하는 불안한 생각이 들때면 이 노래를 찾습니다.")
        
    song3_col1, song3_col2 = st.columns([1, 4])
    with song3_col1:
        st.image("beenzino_3.jpg", use_container_width=True)
    with song3_col2:
        st.markdown("**3. If i die tomorrow**\n\n제목에 나온 것 처럼 누구나 한번 쯤 해봤을 고민을 다루는 노래입니다. 빈지노라는 사람의 삶을 되돌아 보는 가사가 본인 스스로도 다시 한번 생각해보게 합니다.")
    
    st.divider()
    
    st.markdown("### 🎧 상황별 플레이리스트")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("지칠 때", expanded=True):
            st.markdown("""
            * **추천곡 1**: (The anecdote - E SENS)
            * **추천곡 2**: (Gas- E SENS)
            * *설명: 약간은 무겁고 현실적인 노래지만, 거기서 오는 위로와 동기부여가 있습니다.*
            """)
            st.info("💡 **이때의 나의 감정:** 공부 끝나고 집가는 길이나 심적으로 지칠때, 삶의 동기를 찾게 해주는 느낌입니다. ")
            
        with st.expander("전투력이 필요할 때", expanded=True):
            st.markdown("""
            * **추천곡 1**: (25(Feat.양홍원) - 키드밀리)
            * **추천곡 2**: (PUBLIC ENEMIES - Lil Moshpit 외 4인 )
            * *설명: 비트 자체가 무기입니다. 비트를 듣지마자 반응이 오는 노래들*
            """)
            st.info("💡 **전투력 상승:** 공부하기 전에 뭔가 하기싫고 처질때, 이 노래를 들으면 전투력이 상승합니다.")
            
    with col2:
        with st.expander("자기 전 천장보고 듣는 노래", expanded=True):
            st.markdown("""
            * **추천곡 1**: (ROSE - 양홍원)
            * **추천곡 2**: (산책 - GongGongGoo009)
            * *설명: 자기 전에 잡생각하면서 듣기 좋은 노래입니다.*
            """)
            st.info("💡 **잠들기 전 생각:** 최근에는 좋아하던 누나랑 어떻게하면 친해질까 하면서 들었던 것 같습니다...ㅋㅋㅋ ")
            
        with st.expander("🌙 새벽 감성", expanded=True):
            st.markdown("""
            * **추천곡 1**: (seasons - wave to earth)
            * **추천곡 2**: (EVERTHING - 검정치마)
            * *설명: 가만히 듣고 있으면, 행복했던 순간들의 기억을 가져오는 노래들.*
            """)
            st.info("💡 **새벽 감성:** 새벽에 창문 열고 맥주 한캔 들고 듣고있으면 많은 생각이 듭니다 .. ")

    st.divider()

    st.markdown("### 💿 추천하는 앨범")
    st.write("타이틀곡뿐만 아니라 앨범 전체를 처음부터 끝까지 통째로 돌려 듣는 것을 추천하는 명반들입니다.")
    
    col_album1, col_album2, col_album3 = st.columns(3)
    
    with col_album1:
        st.markdown("#### 1. 킁")
        st.write("**C-JAMM**")
        st.info("국힙 정점")
        
    with col_album2:
        st.markdown("#### 2. K-FLIP+")
        st.write("**식케이**")
        st.info("개인적으로 식케이를 좋아하지 않지만, 처음 들었을 때의 느낌은 아직 잊을 수 없습니다..")
        
    with col_album3:
        st.markdown("#### 3. ?")
        st.write("**XXXTENTACION**")
        st.info("어둡고 내면의 복잡한 느낌을 이렇게 잘 살린 앨범은 아직 없음")

with tab3:
    st.subheader("개인적으로 추천하는 책 3권")
    st.write("사실 책을 자주 읽지 않지만, 그래도 읽었던 책 중에 추천해보겠습니다.")
    
    with st.expander("📖 1. 이방인 - 알베르 카뮈", expanded=True):
        col_img, col_text = st.columns([1, 4])
        with col_img:
            st.image("book_1.jpg", use_container_width=True)
        with col_text:
            st.markdown("**오늘 엄마가 죽었다. 아니, 어쩌면 어제**")
            st.write(" 이 책은 제가 가장 여러번 읽은 책인데, 읽을 때마다 느낌이 조금 다릅니다. 처음에는 '뭐라는거지?' 이런 느낌이 강했는데 나중에는 '아 이게 그건가?' 하는 부분이 많아 지더라고요. 읽어본 사람은 공감할 것이라고 생각합니다. 저는 이 책을 읽으면서 '사회가 당연하게 받아들이는 것을 나도 당연하게 따라야 하는 것인가?'라는 생각을 계속 했던 것 같습니다. 그런 부분에서 사회가 강요한 당연함에 대해 생각하는 계기가 됐던 것 같습니다. 다들 꼭 한번은 읽어보길 추천합니다.  ")

    with st.expander("📖 2. 변신 - 프란츠 카프카", expanded=True):
        col_img, col_text = st.columns([1, 4])
        with col_img:
            st.image("book_2.jpg", use_container_width=True)
        with col_text:
            st.markdown("**읽은 뒤 여운이 많이 남았던 책**입니다.")
            st.write("개인적으로 이 책은 다 읽은 뒤 벙찌게(?) 되는 책인 것 같습니다. (뭔가 '어..?' 이런 느낌) 주인공이 어느날 벌레가 되어 죽을 때 까지를 다룬 소설인데, 한 사람으로서의 존엄을 잃어가는 느낌이 무서울 정도로 잘 표현된 작품 같습니다. 읽다보면 주인공이 정말 안쓰럽게 느껴집니다. 죽음을 맞이함으로서 비로소 편안함을 얻는 듯한 주인공을 보면 살아간다는 것이 갖는 의미를 다시 한번 생각하게 합니다. 인생에 현타가 올때나 생각이 복잡해질때 한번쯤 읽어보는 것을 추천합니다.    ")

    with st.expander("📖 3. 누구를 구할 것인가? - 토머스 캐스카트", expanded=True):
        col_img, col_text = st.columns([1, 4])
        with col_img:
            st.image("book_3.jpg", use_container_width=True)
        with col_text:
            st.markdown("**세 번째 추천 책**입니다.")
            st.write("이 책은 기차 딜레마 상황을 중심으로 공리주의적 사고를 다시 한번 생각하게 만드는 책 입니다. 당연하게 느껴졌던 공리주의적 사고를 비판적으로 바라보게 됐습니다. 최대 행복이라는 것 자체가 정량적인 것으로 느껴지는 표현인데, '우리의 삶속에 존재하는 가치를 정량적으로 생각할 수 있는가?' 라는 의문을 갖게합니다. 목숨의 가치를 정량적으로 생각한다는 것과 목숨이 아니더라도 무엇의 가치를 정량적인 것으로 환원하는 발상 자체를 되돌아보는 계기가 됐습니다.  ")

    st.divider()

    st.subheader("👀 앞으로 읽어보고 싶은 책 ")
    st.info("아직 다 읽지는 못했지만, 언젠가 다 읽어보고 싶은 책 입니다..")
    st.markdown("""
    - [ ] **지하로부터의 수기 - 표도르 도스토옙스키**: 이 책은 읽으려도 도전했지만, 초반 부분을 도저히 알아먹을 수 없어서 포기한 책 입니다... 아니 뭐라는지 알아먹을 수가 없어요.. 나중에 다 읽어보려고 합니다.
    - [ ] **사피엔스 - 유발 하라리**: 중간 정도까지는 흥미롭게 읽었던 것 같은데 그 뒤로는 좀 지루해서 유기한 책 입니다. 꼭 끝까지 읽어보겠습니다. 
    - [ ] **코스모스 - 칼 세이건**: 사피엔스랑 같은 이유로 읽다가 유기한 책 입니다. 다시 흥미가 생겨서 다 읽는 날이 언젠가 오지 않을까요..? 
    """)

# 사이드바 구성
with st.sidebar:
    st.markdown("### 📌 빠른 이동 (목차)")
    st.markdown("""
    <style>
    .toc-link {
        display: block;
        padding: 10px 0;
        text-decoration: none;
        color: inherit;
        font-weight: 600;
        font-size: 16px;
    }
    .toc-link:hover {
        color: #ff4b4b;
    }
    </style>
    <a href="#5d5acbc4" target="_self" class="toc-link">🎉 나의 관심사를 소개합니다!</a>
    <a href="#984f9e22" target="_self" class="toc-link">🔍 본격적인 설명 들어갑니다.</a>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("### ✍️ 나만의 취향 기록하기")
    team = st.text_input("⚽ 응원하는 축구팀은?")
    song = st.text_input("🎵 나의 최애곡은?")
    book = st.text_input("📚 추천하는 인생 책은?")
    nickname = st.text_input("😎 본인의 닉네임은?")
    
    if st.button("기록 저장하기"):
        if team or song or book or nickname:
            try:
                # 1. Google Sheets 연결 객체 생성
                conn = st.connection("gsheets", type=GSheetsConnection)
                
                # 2. 기존 데이터 불러오기 (에러 방지를 위해 빈 데이터프레임 대비)
                try:
                    existing_data = conn.read(worksheet="Sheet1", usecols=list(range(5)), ttl=5)
                    existing_data = existing_data.dropna(how="all")
                except Exception:
                    existing_data = pd.DataFrame(columns=["시간", "닉네임", "축구팀", "최애곡", "인생책"])
                
                # 3. 새로운 데이터 행(Row) 생성
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_row = pd.DataFrame([{
                    "시간": current_time,
                    "닉네임": nickname if nickname else "익명",
                    "축구팀": team,
                    "최애곡": song,
                    "인생책": book
                }])
                
                # 4. 기존 데이터와 병합 후 업데이트
                updated_data = pd.concat([existing_data, new_row], ignore_index=True)
                conn.update(worksheet="Sheet1", data=updated_data)
                
                if nickname:
                    st.success(f"{nickname}님의 취향이 성공적으로 기록되었습니다! 🎉")
                else:
                    st.success("취향이 구글 시트에 성공적으로 기록되었습니다! 🎉")
            except Exception as e:
                st.error(f"구글 시트 저장 중 오류가 발생했습니다. (Secrets 설정을 확인해주세요!)\\n{e}")
        else:
            st.warning("내용을 최소 하나 이상 입력해주세요!")
