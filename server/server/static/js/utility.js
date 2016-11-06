    // var map = {};
    // var buf = {};
    // var count = 0;

    $('#comment').bind('input propertychange', function() {
        if(this.value.length){
          // reset();
          $('#showResult').empty();
          // spliteWords(this.value);
          getData(this.value, 'PersonalityInsights');
          getData(this.value, 'AlchemyLanguage');
          getData(this.value, 'ToneAnalize');
        }
    });

    function addItem(header, info) {
      $('#showResult').append('<div class="row"><div class="callout callout-info"><h4>'+header+'</h4><p>'+info+'</p></div></div>');
    }

    // function changeImg(id) {
    //   console.log( $("#" + id));
    //   console.log( $("#" + id).attr("src")); 
    //   var src = $("#" + id).attr("src").replace(".jpg", "quote.jpg");
    //   $("#" + id).attr("src", src);
    // }
    // function changeImgBack(id) {
    //   var src = $("#" + id).attr("src").replace("quote.jpg", ".jpg");
    //   $("#" + id).attr("src", src);
    // }
    // function replace(word, replaceWord) {
    //   var oldText = document.getElementById("comment").value;
    //   patten = new RegExp(word, "g");
    //   var text = oldText.replace(patten, replaceWord);
    //   document.getElementById("comment").value = text;
    //   reset();
    //   spliteWords(text);
    // }

    // function showProblemCount(id) {
    //   $( "#" + id ).html(count);
    // }

    // function spliteWords(text) {
    //   text = text.replace(/[^A-Za-z0-9 ]/g, '');
    //   var strs = text.split(" ");
    //   for(var i = 0; i < strs.length; ++i) {
    //     if(strs[i].length > 0) {
    //       processWord(strs[i]);
    //     }
    //   }
    //   showProblemCount('showCount');
    // }

    // function processWord(word) {
    //   if(map[word] == null) {
    //     var path = "/word/" + word;
    //     $.get(path, function( data ) {
    //       data = jQuery.parseJSON(data);
    //       map[word] = data;
    //       addItems(data, word);
    //     });
    //   }
    //   else {
    //     addItems(map[word], word);
    //   }
    // }

    // function addItems(data, word) {
    //   if(buf[word] == null) {
    //     if(data['information'] != null ) {
    //       addItemInfo("resultInformation", data['information'], word, 'box-info');
    //     }
    //     if(data['warning'] != null ) {
    //       addItemWarn("resultWarning", data['warning'], word, 'box-warning');
    //     }
    //     if(data['substitution'] != null ) {
    //       addItemSub("resultSubstitution", data['substitution'], word);
    //     }
    //     buf[word] = "done";
    //   }
    // }
 
    // function addItemInfo(id, text, word) {
    //   var info = jQuery.parseJSON(text);
    //   count = count + 1;
    //   var html = '<div class="box box-info box-solid"><div class="box-header with-border">';
    //   html += '<h3 class="box-title">' + word + '</h3></div><div class="box-body">';
    //   html += '<p>' + info['describe'] + '<a href="'+info['website']+'"> more</a></p><div class="attachment-block clearfix">';
    //   html += '<img id="person'+info['img']+'" onmouseover="changeImg(\'person'+info['img']+'\')" onmouseout="changeImgBack(\'person'+info['img']+'\')" class="attachment-img" src="static/img/' + info['img'] + '.jpg" onclick="work()">';
    //   html += '<div class="attachment-pushed"><h4 class="attachment-heading"><a href="'+info['webBio']+'">'+info['person']+'</a></h4></div>';
    //   html += '</div></div></div>';
    //   $( "#" + id ).append(html);
    //   $( "#" + id ).removeClass("hide");
    // }
    
    // function addItem(id, text, word, color) {
    //   count = count + 1;
    //   var html = '<div class="box ' + color + ' box-solid"><div class="box-header with-border">';
    //   html += '<h3 class="box-title">' + word + '</h3></div><div class="box-body">';
    //   html += text + '</div>';
    //   $( "#" + id ).append(html);
    //   $( "#" + id ).removeClass("hide");
    // }

    // function addItemWarn(id, text, word, color) {
    //   count = count + 1;
    //   var html = '<div class="box ' + color + ' box-solid"><div class="box-header with-border">';
    //   html += '<h3 class="box-title">' + word + ' ' + text + '</h3>';
    //   $( "#" + id ).append(html);
    //   $( "#" + id ).removeClass("hide");
    // }

    // function addItemSub(id, text, word, color) {
    //   count = count + 1;
    //   var strs = text.split(", ");
    //   var list_button = "";

    //   for(var i = 0; i < strs.length ; ++i) {
    //     list_button += '<button onclick="javascript:replace(\''+word+'\',\''+strs[i]+'\');" type="button"class="btn btn-block btn-danger btn-xs">'+strs[i]+'</button>';
    //   }

    //   var html = '<div class="box box-danger box-solid"><div class="box-header with-border">';
    //   html += '<h3 class="box-title">Please replace ' + word + ' with :</h3></div><div class="box-body">';
    //   html += list_button + '</div>';

    //   $( "#" + id ).append(html);
    //   $( "#" + id ).removeClass("hide");
    // }

    // function remove(id) {
    //   $( "#" + id ).empty();
    //   $( "#" + id ).addClass("hide");
    // }

    // function reset() {
    //   remove("resultSubstitution");
    //   remove("resultInformation");
    //   remove("resultWarning");
    //   count = 0;
    //   buf = {};
    // }

    // // Get the modal
    // var modal = document.getElementById('myModal');

    // // Get the image and insert it inside the modal - use its "alt" text as a caption
    // function work(){
    //     modal.style.display = "block";
    // }

    // // Get the <span> element that closes the modal
    // var span = document.getElementsByClassName("close")[0];

    // // When the user clicks on <span> (x), close the modal
    // span.onclick = function() { 
    //   modal.style.display = "none";
    // }

    // showProblemCount('showCount');
    // reset();