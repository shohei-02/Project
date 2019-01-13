var data = [
    new MyModel('先行', '', ''),
    new MyModel('後攻', '', '')
];

var grid = document.getElementById('grid');

new Handsontable(grid, {
    data: data,
    dataSchema: new MyModel(), // ★空のインスタンスを渡す
    columns: [
        {
            // ★セルの値が参照・変更されたときにコールバックされるので、
            //   第二引数に値が渡されたかどうかでモデルから値を取得するか、
            //   値を設定するかを決める。
            data: function(myModel, name) {
                if (name) {
                    myModel.setName(name);
                } else {
                    return myModel.getName();
                }
            }
        },
        {
            data: function(myModel, ini1) {
                if (ini1) {
                    myModel.setIni1(ini1);
                } else {
                    return myModel.getIni1();
                }
            }
        },
        {
            data: function(myModel, ini2) {
                if (ini2) {
                    myModel.setIni2(ini2);
                } else {
                    return myModel.getIni2();
                }
            }
        }
    ]
});

// ボタンをクリックしたら、現在の data の内容を表示する
document.getElementById('button').addEventListener('click', function() {
    data.forEach(function(myModel) {
        console.log(myModel.toString());
    });
});

// 独自クラス
function MyModel(name, ini1, ini2) {
    var _name = name,
        _ini1 = ini1,
        _ini2 = ini2;

    this.getName = function() {
        return _name;
    };

    this.setName = function(name) {
        _name = name;
    };

    this.getIni1 = function() {
        return _ini1;
    };

    this.setIni1 = function(ini1) {
        _ini1 = ini1;
    };

    this.getIni2 = function() {
        return _ini2;
    };

    this.setIni2 = function(ini2) {
        _ini2 = ini2;
    };

    this.toString = function() {
        return 'MyModel{name=' + _name + ', ini1=' + _ini1 + ', ini2=' + _ini2 + '}';
    };
}

