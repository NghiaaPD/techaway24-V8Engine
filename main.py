import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="V8 Engine",
    page_icon="./assets/icons/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.write(
    """
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .img-container {
        margin-bottom: 20px;
    }
      h1 {
        font-size: 80px;
    }
    </style>
    <div class="container">
        <div class="img-container">
            <img src="https://appetiser.com.au/wp-content/uploads/2019/03/Google-V8.png.webp" width="700" style="channels='RGB'">
        </div>
        <h1>V8 Engine</h1>
        <p>Đây là nội dung của bạn.</p>
        <!-- Thêm nội dung của bạn sau đây -->
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Nội dung bài viết")
    source_vid = st.sidebar.write("""
    <style>
        .toc {
            background-color: #0E1117;
            border-radius: 10px;
        }
        .toc p {
            font-size: 15px;
            margin: 0;
            padding: 10px;
            cursor: pointer;
            z-index: 2;
        }
        # .toc p:nth-child(odd) {
        #     background-color: #F1F1EF; /* Màu nền cho các hàng lẻ */
        # }
        # .toc p:nth-child(even) {
        #     background-color: #262730; /* Màu nền cho các hàng chẵn */
        # }
    </style>
    <div class="toc">
        <p>1. Giới thiệu tổng quát V8 Engine</p>
        <p>2. Fast Property Access</p>
        <p>3. Garbage Collection</p>
        <p>4. Pipeline</p>
        <p>5. Tổng kết</p>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Post", "Demo", "Reference"])

with tab1:
    st.markdown("<h2 style='color: #FFC81B;'>F-Code [Techaway 2024]</h2>", unsafe_allow_html=True)
    st.markdown("#### **F-Code authors:**")
    st.write("""
        - *Trần Anh Kiệt - F19*
        - *Nguyễn Lâm Tài Lợi - F19*
    """)
    st.header("Lời mở đầu")
    st.write("""
    Xin chào mọi người! Có lẽ nếu đã tìm hiểu về ngôn ngữ JavaScript, mọi người ít nhất cũng đã nghe qua về Node.js. Tuy nhiên, liệu các bạn đã từng thắc mắc bên trong Nodejs có những gì không? Hôm nay, chúng mình muốn chia sẻ với các bạn về V8 Engine – trái tim của Node.js. Ở bài viết này chúng ta sẽ tìm hiểu về từng thành phần và hoạt động của nó. 

    Bài viết này còn nhiều điểm thiếu sót, hy vọng các bạn đọc xong sẽ góp ý kiến cho bọn mình, cũng như thu về cho bản thân được một ít thông tin, để từ đó có thể hiểu thêm và đào sâu về engine này.
    """)

    st.markdown("<h2 style='color: #51C95D;'>1. Giới thiệu về V8 Engine</h2>", unsafe_allow_html=True)
    st.write("""
    - V8 là một công cụ mã nguồn mở hiệu suất cao, được phát triển bởi Google, chuyên xử lý JavaScript và WebAssembly. Được viết bằng ngôn ngữ lập trình C++, V8 được sử dụng rộng rãi trong các dự án như Google Chrome, Chromium và Node.js, cùng với nhiều ứng dụng khác trên nền tảng web.
    - V8 đã được chọn làm công cụ hỗ trợ Node.js vào năm 2009 và khi mức độ phổ biến của Node.js bùng nổ, V8 đã trở thành công cụ hiện cung cấp một lượng server-side code đáng kinh ngạc được viết bằng JavaScript.
    - V8 là một JavaScript engine, nó phân tích và thực thi code JavaScript, xử lý việc cấp phát bộ nhớ cho các đối tượng (object) và thu dọn các object mà nó không còn cần nữa. DOM và các API nền tảng web khác (runtime environment) đều do trình duyệt (Google Chrome) cung cấp. 
    """)
    st.write(
        """
        <style>
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .img-container {
            margin-bottom: 20px;
        }
        </style>
        <div class="container">
            <div class="img-container">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/V8_JavaScript_engine_logo_2.svg/1200px-V8_JavaScript_engine_logo_2.svg.png" width="500" style="channels='RGB'">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("""
    - V8 là mô hình đầu tiên được tạo ra nhằm mục đích tăng tốc độ thực thi của JavaScript trên web browsers. Để đạt được tốc độ tối ưu, V8 engine biên dịch mã code JavaScript thành một mã code hiệu quả hơn thay vì sử dụng một thông dịch viên (interpreter). Nó sẽ biên dịch JavaScript thành ngôn ngữ máy khi thực thi bằng việc xây dựng một JIT (Just-In-Time) compiler cũng tương tự như nhiều engine khá nổi tiếng khác đã làm như SpiderMonkey hay Rhino (Mozilla). Sự khác biệt chính ở đây là V8 không xuất ra bytecode hay bất kỳ một mã code trung gian nào.
    """)

    st.markdown("<h2 style='color: #51C95D;'>2. Fast Property Access</h2>", unsafe_allow_html=True)
    st.write("""
    - #### *Hidden Class*
        - Mọi thứ trong JavaScript đều là một Objects và attributes của Object đều có thể được thêm hoặc xóa hoặc thay đổi loại dữ liệu bất kỳ lúc nào. Điều này làm cho việc tối ưu hóa một ngôn ngữ "động" như JavaScript trở nên khó khăn. Ví dụ Code dưới đây:
            
        - Có thể thấy hàm `openTheDoor()` nhận một đối tượng và gọi hàm `openDoor()` của đối tượng đó. Tuy nhiên, do không có cách nào để chỉ định kiểu dữ liệu đầu vào của hàm `openTheDoor` nên trình biên dịch sẽ không biết đối tượng nhận được có hợp lệ hay không, có chức năng `openDoor()` hay không. Trong trường hợp bạn phải kiểm tra bằng tra cứu . Rõ ràng nó sẽ giảm hiệu suất đi rất nhiều. Nguyên nhân có lẽ nằm ở thiết kế của JavaScript.
    """)
    code_1 =   '''
        class Car {
            openDoor() {
            // Code block
            }
        }
        
        class Human {
            // Human has no door
        }
        
        const openTheDoor = (object) => {
            object.openDoor();
        }
        '''
    st.code(code_1, language='javascript')
    st.write("""
    **Hidden Class** được tạo ra để giải quyết vấn đề này. **Hidden Class** được gán cho từng đối tượng để giúp việc theo dõi types và attribute của chúng thuận tiện hơn. Object thay đổi thì **Hidden Class** cũng thay đổi tương ứng.
    """)
    code_2 = '''
    const point = {}
    point.x = 0;
    point.y = 1;
    '''
    st.code(code_2, language='javascript')
    st.write("""
    Đoạn code trên sẽ phải thay đổi cấu trúc của object **point** 3 lần. Một là ở câu lệnh `const point = {}`, lúc này V8 sẽ tạo ra **hidden class** tạm gọi là **C0** để biểu diễn cấu trúc của **point** (một **object** rỗng). Và khi câu lệnh gán `point.x` thì **object** thay đổi, nên V8 lúc này sẽ thay thế hidden class **C0** thành **C1** (có thêm thuộc tính .x). Và cuối cùng là **C2** (có thêm thuộc tính .y), quá trình được diễn ra như sau:
    """)
    st.image("https://ren0503.github.io/assets/img/v8/hidden_class1.png", width=1000, channels="RGB")
    st.write("Đoạn code trên giúp ta hiểu về cách hoạt động của hidden class, và đây là cách tối ưu:")
    code_3 = '''
    let point = {
        x: 0,
        y: 1,
    };
    '''
    st.code(code_3, language='javascript')
    st.image("https://ren0503.github.io/assets/img/v8/hidden_class2.png", width=800, channels="RGB")
    st.write("""
    Vì không có gì khác biệt sau khi thay đổi nên Hidden Class chỉ cần tạo 1 lần thôi, tối ưu được hiệu xuất.
    
    Các object có cùng kiểu hoặc cấu trúc (hoặc thuộc cùng một class) thì sẽ có chung một hidden class, V8 sẽ không tạo mới mà tái sử dụng các hidden class đã có nếu trùng khớp.
    Ví dụ với câu lệnh sau, hidden class của point thay đổi từ C2 về lại C1 chứ không tạo mới:
    """)
    code_4 = '''
    delete point.y;
    '''
    st.code(code_4, language='javascript')
    st.image("https://ren0503.github.io/assets/img/v8/hidden_class3.png", width=1000, channels="RGB")
    st.write("""
    Tuy nhiên, nếu thuộc tính bị xóa là .x thì sẽ lại có một hidden class C3 được tạo ra. Bằng cách sử dụng hidden class, V8 có thể biết trước được cấu trúc của một class/object, từ đó tối ưu việc truy xuất đến các thuộc tính của chúng bằng nhiều cách, một trong các kĩ thuật tối ưu mà V8 áp dụng đó là ***inline caching***.
    """)

    st.write("""
    - #### *Inline caching*
    """)
    code_5 = '''
    function getX(o) {
        return o.x;
    }
    '''
    st.code(code_5, language='javascript')
    st.write("Khi chạy function này sẽ sinh ra bytecode như sau:")
    st.image("https://ren0503.github.io/assets/img/v8/inline_caching1.png", width=600, channels="RGB")
    st.write("""
    Câu lệnh `get_by_id` nhận thuộc tính x từ tham số đầu tiên `(arg1)` và lưu kết quả vào `loc0`. Câu lệnh thứ 2 trả về `loc0`.
    Compiler cũng nhúng inline cache vào lệnh `get_by_id`, trong đó có 2 slot chưa được khởi tạo
    """)
    st.image("https://ren0503.github.io/assets/img/v8/inline_caching2.png", width=600, channels="RGB", caption="Shape trong hình là Hidden Class")
    st.write("""
    Giả sử mình gọi `getX` với object là `{x: 'a'}`. Như đã nói, object này có một hidden class chứa thuộc tính x mà chỉ lưu offset và đặc tính của thuộc tính x. Khi mà function này chạy lần đầu tiên thì `get_by_id` sẽ tìm kiếm `x` và tìm thấy giá trị được lưu ở offset 0.
    """)
    st.image("https://ren0503.github.io/assets/img/v8/inline_caching3.png", width=600, channels="RGB")
    st.write("Inline cache được nhúng trong `get_by_id` sẽ lưu lại hidden class cũng như offset:")
    st.image("https://ren0503.github.io/assets/img/v8/inline_caching4.png", width=600, channels="RGB")
    st.write("Với những lần chạy tiếp theo, inline cache chỉ cần so sánh hidden class, nếu trùng với cái đã có thì chỉ cần tải giá trị từ bộ nhớ. Cụ thể, nếu V8 tìm thấy object với hidden class mà inline cache đã ghi lại trước đó, nó sẽ không cần phải tìm thông tin về thuộc tính nữa, phần tìm kiếm này sẽ bị bỏ qua hoàn toàn. Nên sẽ thật sự nhanh hơn việc phải tìm kiếm thuộc tính lại mỗi lần chạy hàm.")

    st.markdown("<h2 style='color: #51C95D;'>3. Garbage Collection</h2>",
                unsafe_allow_html=True)

    st.write("""
    *Garbage Collection (GC)* – hay gọi vui là công ty môi trường đô thị. GC thực hiện công việc dọn rác (thu gom và xóa những object/value không còn dùng đến, trả không gian bộ nhớ cho các tác vụ khác). Đây là một phần quan trọng nhưng ít được chú ý trong JavaScript.  Trước đây nhiều người vẫn hay nói đùa là "JavaScript thì cần gì GC, chạy trên browser, khi nào hết memory user nó F5 một phát thì tất cả rác bay biến hết rồi còn đâu". Ngày nay, khi mà JavaScript đã có nhiều ứng dụng cho xây dựng server lẫn các single page application, vòng đời của một app JavaScript ngày một dài ra, vai trò của GC ngày một lớn.
    
    *GC* của V8 là một *Generational Garbage Collector*. Trong quá trình thực thi, các giá trị (biến, object,...) được tạo ra nằm trong bộ nhớ *heap*. V8 chia *heap* ra làm nhiều khu vực, trong đó ta chỉ đề cập đến hai khu vực chính là *new-space* (chứa các đối tượng nhỏ, có vòng đời ngắn) và *old-space* (chứa các thành phần sống dai hơn, bự hơn).
    
    Hai khu vực này cũng là hai đối tượng cho hai loại thuật toán GC khác nhau, đó là *scavenge* và *mark-sweep/mark-compact*.
    """)
    st.image("https://ren0503.github.io/assets/img/v8/garbage_collection1.png", width=1000, channels="RGB")
    st.write("""
    Khi chúng ta khai báo một giá trị mới, giá trị này sẽ được cấp phát nằm rải rác trong khu vực new-space, khu vực này có một kích thước nhất định, thường là rất nhỏ (khoảng 1MB đến 8MB, tùy vào cách hoạt động của ứng dụng). Việc khai báo như thế này tạo ra nhiều khoảng trống không thể sử dụng được trong bộ nhớ.
    
    Khi **new-space** đã đầy, thì **scavenge** sẽ được kích hoạt để dọn dẹp các vùng nhớ "chết", giải phóng mặt bằng, có thể sẽ gom góp các vùng nhớ rời rạc lại gần nhau cho hợp lý, vì **new-space** rất nhỏ, nên **scavenge** được kích hoạt rất thường xuyên. Trong quá trình giải tán đô thị của **scavenge**, nếu các vùng nhớ nào còn trụ lại được sau **2** chu kỳ, thì sẽ được chuyển lên khu vực **old-space**, nơi mà có sức chứa lớn hơn lên đến hàng trăm megabytes, và là nơi mà thuật toán **mark-sweep** hoặc **mark-compact** hoạt động, với chu kỳ dài hơn, ít thường xuyên hơn.
    """)

    df_3 = pd.DataFrame(
        [
            {"command": "Scavenger GC ( bộ thu hồi rác Lao Công A)",
             "main_cpl": "Mark-Sweep GC ( bộ thu hồi rác Lao Công B)",
            },
            {"command": "Lao Công A",
             "main_cpl": "Lao Công B",
            },
            {"command": "Lau nhiều lần trong 1 ngày ( 1 khoảng thời gian để đo lường), Lau nhanh",
             "main_cpl": "Lau với tuần suâất ít hơn Lao Công A, Lau chậm",
            },
        ]
    )

    edited_df_3 = st.data_editor(
        df_3,
        key="unique_key_for_df_3",  # Unique key for this data editor widget
        width=1200,
        column_config={
            "command": st.column_config.Column(
                "NewSpace",
                width="medium",
            ),
            "main_cpl": st.column_config.Column(
                "OldSpace",
                width="medium",
            ),
        },
        hide_index=True,
        disabled=["command", "main_cpl"],
    )

    st.write("""
    Tất cả những thuật toán GC trên đều hoạt động thông qua hai bước chính là:
    - Bước đánh dấu: thuật toán sẽ duyệt qua tất cả các giá trị có trong khu vực bộ nhớ mà nó quản lý, bước duyệt này đơn giản chỉ là thuật toán **depth-first search (dfs)**, tìm gặp và đánh dấu.
    
    - Bước xử lý: sau quá trình duyệt, tất cả những giá trị chưa được đánh dấu, sẽ bị coi là đã "chết", và sẽ bị xóa bỏ, trả lại bộ nhớ trống (`sweep`), hoặc gom góp lại để lấy lại các khoảng trống trong bộ nhớ không sử dụng được (`compact`).
    
    Điểm khác nhau giữa scavenge và mark-sweep/mark-compact nằm ở cách mà chúng được triển khai. Chi tiết: [A tour of V8: Garbage Collection](https://jayconrod.com/posts/55/a-tour-of-v8-garbage-collection) .
    """)
    code_6 = '''
    let obj1 = { name: "huy" };
    // tạo 1 đối tượng mới
    let obj2 = { name: "quynh" };
    // tạo 1 đối tượng khác

    obj1 = null;
    // không còn tham chiếu đến obj1
    '''
    st.code(code_6, language='javascript')
    st.write("""
    Khi đoạn mã này được thực thi, đối tượng obj1 được tạo ra và lưu trữ trong bộ nhớ. Sau đó,  obj2 cũng được tạo ra và lưu trữ trong bộ nhớ.
    
    Sau dòng lệnh obj1 = null, không còn tham chiếu nào đến đối tượng obj1 nữa. Điều này có nghĩa là đối tượng obj1 đã không còn được truy cập từ bất kỳ điểm nào trong mã JavaScript nữa.
    
    Khi bộ thu gom rác của V8 chạy, nó sẽ quét qua bộ nhớ và phát hiện ra rằng không còn tham chiếu nào đến đối tượng obj1. Do đó, bộ thu gom rác sẽ thu hồi bộ nhớ được cấp phát cho đối tượng obj1, giải phóng không gian bộ nhớ và loại bỏ rủi ro về rò rỉ bộ nhớ.
    """)

    st.markdown("<h2 style='color: #51C95D;'>4. Cách cài đặt Pipeline</h2>", unsafe_allow_html=True)

    st.write("Các JavaScript engine sử dụng một pipeline gồm trình thông dịch (interpreter) và bộ biên dịch tối ưu (Optimising compiler) để thực thi mã JavaScript hiệu quả. Trình thông dịch sinh ra bytecode nhanh chóng từ mã nguồn JavaScript, trong khi bộ biên dịch tối ưu tạo ra mã máy tối ưu từ bytecode đã sinh. Quá trình này giúp cải thiện hiệu suất thực thi mã JavaScript, với trình thông dịch cung cấp sự nhanh chóng và bộ biên dịch tối ưu tạo ra mã máy tối ưu hóa để đạt được hiệu suất cao hơn.")
    st.image("https://ren0503.github.io/assets/img/v8/pipeline1.png", width=700, channels="RGB")
    st.write("Trong V8, trình thông dịch là Ignition còn trình biên dịch là TurboFan.")
    st.image("https://ren0503.github.io/assets/img/v8/pipeline2.png", width=700, channels="RGB")
    st.write("""
    - #### **Ignition**: 
    Ignition là một phần của JavaScript engine của V8, đây là một trong những thành phần quan trọng của Chrome và các trình duyệt web khác. Ignition đảm nhiệm việc phân tích cú pháp và biên dịch mã JavaScript thành mã bytecode thay vì biên dịch trực tiếp thành mã máy như trước đây. 
    
    Trước khi có Ignition, V8 sử dụng một trình biên dịch JIT (Just-In-Time) để biên dịch mã JavaScript thành mã máy trước khi thực thi. Đoạn code được dịch bởi JIT sẽ tiêu hao một lượng tương đối bộ nhớ. Thế nên Ignition ra đời biên dịch code thành bytecode, với chi phí lưu trữ chỉ 25-50% so với phương pháp cũ.

    Kết hợp với TurboFan mã bytecode lúc này có thể xử lý bình thường mà không cần phải biên dịch lại từ đầu.
    
    - #### **TurboFan**:
    TurboFan trong V8 JavaScript engine là một bộ tối ưu hóa mã máy. Khi mã JavaScript được thực thi nhiều lần, TurboFan sẽ tăng dần trạng thái của nó từ "cold" sang "warm" , và cuối cùng là "hot" (nóng). Trong trạng thái "hot", TurboFan sử dụng các thông tin thu thập được về mẫu thực thi để tối ưu hóa mã thành các đoạn mã máy hiệu quả hơn, cải thiện hiệu suất thực thi của ứng dụng JavaScript. Điều này giúp cải thiện tốc độ và hiệu suất của các ứng dụng web chạy trên trình duyệt Chrome.
    """)
    st.image("https://ren0503.github.io/assets/img/v8/pipeline3.png", width=700, channels="RGB")

    st.markdown("<h2 style='color: #51C95D;'>5. Tổng Kết</h2>", unsafe_allow_html=True)
    st.write("Ở trên là các khái niệm về các thành phần trong V8 Engine. Mong là bài viết sẽ có ích với những ai đang muốn tìm hiểu về V8 và Node.js.")

with tab2:
  st.write("# *Không có Demo cho bài này*")

with tab3:
    # Create two columns with a ratio of 1:2
    col1, col2 = st.columns([1, 2])

    # In the first column, display the image
    with col1:
        pass

    # In the second column, display the heading
    with col2:
        st.image("./assets/images/F-Code_logo.png", width=280)
        st.markdown("<h2 style='color: #FFC81B;'>Nguồn Tham Khảo</h2>", unsafe_allow_html=True)
    st.write("")
    st.write("""
            - [Node.js — The V8 JavaScript Engine](https://nodejs.org/en/learn/getting-started/the-v8-javascript-engine)

            - [Documentation · V8](https://v8.dev/docs)

            - [Garbage collection (javascript.info)](https://javascript.info/garbage-collection)

            - [Bên Trong Node.js - V8 Chrome Engine](https://viblo.asia/p/ben-trong-nodejs-v8-chrome-engine-3P0lP8M4lox#_tham-khao-8)

            - [Câu chuyện giữa Anh Chàng NodeJS và Cô Nàng V8](https://hocjavascript.net/node-js/anh-chang-nodejs-va-co-nang-v8/)

            - [A tour of V8: Garbage Collection](https://jayconrod.com/posts/55/a-tour-of-v8-garbage-collection)

            """)
