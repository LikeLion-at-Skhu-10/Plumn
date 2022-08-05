function length_check() {
    var desc = $("#story").val();
  
    if( desc.length > 30 ) {
        alert("제목은 30자를 초과할 수 없습니다.");
        $("#story").val(desc.substring(0, 30));
    }
  }