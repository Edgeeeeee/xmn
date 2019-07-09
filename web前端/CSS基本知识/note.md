# CSS
- 为了让网页元素的样式更加丰富
- 也为了让网页的内容和样式能拆分开
- CSS由此思想而诞生
- CSS是层叠样式表
- html只负责文档的结构和内容，表现形式完全交给CSS，html文档变得更加简洁

# CSS基本语法及页面引用
- CSS基本语法
    - CSS的定义方法是：选择器{属性：值， 属性：值， 属性：值}
    - 选择器是将样式和页面元素关联起来的名称，属性是希望设置的样式属性，每一个属性有一个或者多个值
    - 例如：div{width:100px, height:100px, color:red}
    
- CSS页面引入方法
    - 外联式：通过link标签，链接到外部样式表到页面中。
        
            <link rel="stylesheet" type="text/css" href="css/main.css>
    - 嵌入式：通过style标签，在网页上创建潜入的样式表。
        
            <style type="text/css">
                div{width:100px, height:100px, color:red}
                ......
            </style>
            
    - 内联式: 通过标签的style属性，在标签上直接写样式。
        
            <div style="width:100px, height:100px; color:red">
            ......
            </div>
            
    - 优先级：内联式 > 嵌入式 > 外联式  html页面从上往下加载，下面的会将上面的覆盖

# CSS选择器
- 标签选择器
    - 此种选择器影响范围较大，建议尽量应用在层级选择器中。
    - 举例
    
            div{
                属性：值；
                属性：值；
                属性：值；
            }
    
- id选择器
    - 通过id名来选择元素，元素的id名称不能重复，所以一个样式只能应用于页面上的一个元素，不能复用
    - id名一般给程序使用，所以一般不推荐使用id作为选择器。
    - 举例
           
            #box(color:red)
            <div id="box">......</div>
            
- 类选择器
    - 通过类名来选择元素，一个类可应用于多个元素，一个元素上也可以使用多个类，应用灵活，可复用，是CSS种应用最多的一种选择器
    - 举例
    
            .red{color:red}
            .big{font-size:20px}
            .nt10{nargin-top:10px}
            <div class="red">......</div>
            <div class="red nt10" big>......</div>
            <div class="red nt10">......</div>
            
            
- 层级选择器
    - 主要应用在选择父元素下的子类元素,或者子元素下面的子元素,可与标签元素结合使用,同时也可以通过层级,防止命名冲突.
    
- 组选择器
    - 多个选择器设置同样的样式,可以使用组选择器,也成为并列选择.
    
            .box1, .box2, .box3{
                ......
            }
            
- 伪类及伪元素选择器
    - 常用的伪类选择器有hover,表示鼠标悬停在元素上的状态.
    - 伪元素选择器有before和after,他们可以通过样式在元素中插入内容.
    
    
# CSS颜色,文本字体
- CSS颜色表示法
    - 颜色名表示 比如:red,yellow
    - 16进制数值表示,比如#f0000,一共有六位值.前两个数值代表红色,中间代表绿色,最后两位代表蓝色.取值范围为0到15
        - \#000000代表黑色 \#ffffff代表白色
    - RGB颜色:红(R),绿(G),蓝(B) background-color:rgb(100,200,0)
    - RGBA颜色:红,绿,蓝,透明度 background-color:tgba(100, 200, 0, 0.5)
    - 注意 rgb的值为1到255
- CSS文本设置
    - color 设置文本颜色,如color:red;
    - font-size 设置文字的大小,如font-size:12px;
        - 谷歌默认16size,最小大小为12px
    - font-family 设置文字的字体,如font-size:"微软雅黑";
        - 设置的字体不存在时候以默认(微软雅黑)显示
    - font-style 设置文字是否倾斜,如font-style:'normal'为不倾斜,font-style:'italic'为倾斜.
    - font-weight 设置文字是否加粗,如font-weight:bold;为加粗,normal为不加粗
    - font-height 设置文字的行高 如font-height:24px;
        - 设置单行文本垂直居中,值给父级元素高度
        
                .item2{
                    width:500px;
                    heiget:200px;
                    background-color:green;
                    /*font-height设置单行的文本居中*/
                    font-height:200px;    
                }
    - text-decoration 设置文字的下划线,如text-decoration:none;将下划线去掉,一般都是给a标签去掉下划线.
        
               a{
                    text-decoration:none;
                }
                <a href="http://www.baidu.com">百度</a>
               
    - text-indent 设置文字首行缩进,如 text-indent:24px;设置文字首行缩进24px
    - text-align 设置文字水平对齐方式,如text-align:center 设置文字水平居中.
    
- CSS边框属性
    - border:宽度 样式 颜色  顺序部分前后 三个值都要写，一个都不能少。
    - border-left：宽度 样式 颜色  单独设置左侧边框 同样要写三个值，top，right，bottom分别为上，右，下。
    - border-color;
    - border-style; 边框样式,solid 实线,dotted 点状线, dashed 虚线
    - border-width;
    - border-left-color;
    - border-lift-style
    - border-lift-width
    - border-radius：3px; 圆角处理3px
        - 如果给一个值 则同时设置四个角，也可以给4个值 顺时针方向对应，若果给两个值，则为对角设置。
    - box-shadow: x轴偏移 y轴偏移 模糊度 扩散程度 颜色 insert内阴影 设置或检索对象阴影
    
            .box{
                width:200px;
                height:200px;
                border:solid red 1px;
                box-shadow:10px 20px 20px 10px red [insert]; 如果设置了insert 则为内阴影。
                <!-- 自己设置，在浏览器种调 ，可以设置负值-->
            }
            
- 背景属性
    - background-color：red； -color可以省略
    - background-image:背景图片 background-image：url（图片地址，本地或网络）
    - background-repeat：是否重复，如何重复，平铺？
        - background-repeat：no-repeat：设置重复
        - 背景图片组合写法：background：url(地址) no-repeat
    - background-position：定位 
        - 注意，在网页当中，让图片或者元素往上移动或者往左移动，都要用负值
    - background-size：背景大小，如background-size：100px 140px，或者用百分比。
    
    
# CSS间距
- 内补白（内补丁）
    - 内边距：元素距离元素内部元素的距离
    - padding：检索或设置对象四边的内部边距，如padding:10px;   padding:5px 10px;
    - padding-top: 检索或设置对象顶边的边距 同时还有right，bottom，left。
    - 注意：在使用padding的时候会改变元素的实际大小。
    - 可以同时设置多个。 padding：10px 20px 30px 40px，  上右下左顺序，顺时针。   padding：10px 30px；  上下  设置一个值为四边。
- 外补白（外补丁）
    - margin：检索或设置对象四边的外延边距，如margin：10px;    
        - margin 5px auto;  设置元素水平居中 上下5px margin常用的一种技巧。 auto只能设置左右，不能设置垂直居中。
        - margin设置负值可以让边框合并。
    - margin-top: 检索或设置对象定边的外延，同时还有right，bottom， left。
    
    
# 盒子模型
- 元素页面显示成一个方块，类似一个盒子，CSS盒子模型就是使用现实中的模型来做比喻，帮助我们设置元素的对应样式。
- 把元素叫做盒子，设置对应的样式为，盒子的边框border，盒子的内容和边框之间的距离padding， 盒子与盒子之间的间距margin
- 盒子真实宽度  = width + padding左右 + border左右
- 盒子真实高度  = height + padding上下 + border上下
- 解决padding和border改变盒子实际大小的问题。
    - 改变元素距离内容的间距，但是又不想改变盒子的大小 设置属性 box-sizing：border-box； 一般用的比较多，解决边框占据盒子大小。
    
# 块元素，内联元素，内联块元素
- 元素就是标签，布局中常用的又三种标签，块元素，内联元素，内联快元素，了解这三种属性的特性，才能熟练的进行页面布局。
- 块元素
    - 也可以称为行元素，布局中常用的标签，如div，p，ul，li，h1到h6，dl，dt，dd等都是块元素。他们在布局中的行为：
        - 支持全部的样式
        - 如果没有设置宽度，则默认为父级宽度的100%
        - 盒子占据一行，即使设置了宽度。
        
- 内联元素
    - 也可以称为行内元素，布局中常用的标签如：a，span，em，b，strong等等都是内联元素，他们在布局中的行为：
        - 支持部分样式（不支持宽，高，margin上下）
        - 宽高由内容决定
        - 盒子并在一行
        - 代码换行，盒子之间会产生间距
        - 子元素是内联元素，父元素可以用text-align属性设置子元素的对齐方式，用line-height属性值设置垂直对齐方式
- 内联块元素
    - 也叫行内块元素，是新增的元素类型，现有的元素没有归于此类的，img和input元素的行为类似这种元素，但是也归类于内联元素，他们再布局中的行为：
        - 支持全部样式
        - 如果没有设置宽高，宽高由内容决定
        - 盒子并在一行
        - 代码换行，盒子会产生间距
        - 子元素是内联块元素，父元素可以用text-align属性设置字元素水平对齐方式，用line-height属性值设置垂直对齐方式
        
- 块元素，内联元素，内联块元素之间的转换
    - display属性是用来设置元素的类型及隐藏的，常用的属性有
        - none元素隐藏且不占位置
        - block 元素以块元素显示
        - inline 元素以内联元素显示
        - inline-book元素以内联块元素显示
        
        
# 浮动
### 文档流
- 文档流，是指盒子按照html标签编写的顺序依次从上到下，从左到右排列，块元素占一行，行内元素在一行之内从左到右排列，先写的先排列，后写的排在后面
每个盒子都占据自己的位置

### 浮动的特性
- 浮动元素有左浮动（float：left）和右浮动（float：right）两种
- 浮动的元素会向左或向右浮动，碰到父元素的边界，浮动元素，未浮动的元素才会停下来
- 相邻的浮动元素可以并在一行，超出父级宽度就换行
- 浮动元素后面没有浮动的元素会占据浮动元素的位置，没有浮动的元素内的文字会避开浮动的元素，形成文字绕图的效果
- 父元素内整体浮动的元素无法撑开父元素，需要清除浮动
- 浮动元素之间没有垂直margin的合并

### 清除浮动
- 父级上增加属性overfl：hidden
- 在最后一个子元素的后面加一个空的div，给他样式属性clear：both（不推荐）
- 吃用成熟的清浮动样式类，clearfix

        .clearfix:after, .clerrfix:before{content:'';dispaly:table;clear:both;} 一般用after，要给父级添加
        .clearfix::after{clear:both;}
        clearfix{zoom:1;}
        
- 清除浮动的使用方法：

        .con2{... overflow:hidden}
        或者
        <dv class='con2 clearfix'>
        
        
# 定位
# 关于定位
- 我们可以使用css的position属性来设置元素的定位类型，position的设置项如下
    - relative 生成相对定位元素，元素所占的文档流的位置不变，元素本身相对文档流的位置进行偏移
    - absolute 生成绝对定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于上一个
    设置了相对或者绝对或者固定定位的父级元素来定位，如果找不到，则会相对于body定位
    - fixed 生成固定定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于浏览器窗口进行定位。
    - static 默认值，没有定位，元素出现在正常的文档流中，相当于取消定位属性或者不设置定位属性
- 定位元素特性
    - 绝对定位和固定定位的块元素和行内元素会自动转化为行内块元素
-定位元素的同级
    - **定位元素是浮动在正常的文档流之上的，可以用z-index属性来设置元素的层级** 
