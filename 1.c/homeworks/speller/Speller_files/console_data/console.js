(function(a){function b(d){if(c[d])return c[d].exports;var e=c[d]={i:d,l:!1,exports:{}};return a[d].call(e.exports,e,e.exports,b),e.l=!0,e.exports}var c={};return b.m=a,b.c=c,b.d=function(a,c,d){b.o(a,c)||Object.defineProperty(a,c,{configurable:!1,enumerable:!0,get:d})},b.n=function(a){var c=a&&a.__esModule?function(){return a['default']}:function(){return a};return b.d(c,'a',c),c},b.o=function(a,b){return Object.prototype.hasOwnProperty.call(a,b)},b.p='',b(b.s=82)})({0:function(a,b){'use strict';Object.defineProperty(b,'__esModule',{value:!0});var c=function(a){window.addEventListener('message',function(b){var c=b.source,d=null;try{d=JSON.parse(b.data)}catch(a){return}a(d,c)})},d=function(a){browser.runtime.onMessage.addListener(a)};b.default={BACKGROUND_OPERATION:'background.operation',CONSOLE_UNFOCUS:'console.unfocus',CONSOLE_ENTER_COMMAND:'console.enter.command',CONSOLE_ENTER_FIND:'console.enter.find',CONSOLE_QUERY_COMPLETIONS:'console.query.completions',CONSOLE_SHOW_COMMAND:'console.show.command',CONSOLE_SHOW_ERROR:'console.show.error',CONSOLE_SHOW_INFO:'console.show.info',CONSOLE_SHOW_FIND:'console.show.find',FOLLOW_START:'follow.start',FOLLOW_REQUEST_COUNT_TARGETS:'follow.request.count.targets',FOLLOW_RESPONSE_COUNT_TARGETS:'follow.response.count.targets',FOLLOW_CREATE_HINTS:'follow.create.hints',FOLLOW_SHOW_HINTS:'follow.update.hints',FOLLOW_REMOVE_HINTS:'follow.remove.hints',FOLLOW_ACTIVATE:'follow.activate',FOLLOW_KEY_PRESS:'follow.key.press',FIND_NEXT:'find.next',FIND_PREV:'find.prev',OPEN_URL:'open.url',SETTINGS_RELOAD:'settings.reload',SETTINGS_CHANGED:'settings.changed',SETTINGS_QUERY:'settings.query',onWebMessage:c,onBackgroundMessage:d,onMessage:function(a){c(a),d(a)}}},1:function(a){function b(a,b){var d=a[1]||'',e=a[3];if(!e)return d;if(b&&'function'==typeof btoa){var f=c(e),g=e.sources.map(function(a){return'/*# sourceURL='+e.sourceRoot+a+' */'});return[d].concat(g).concat([f]).join('\n')}return[d].join('\n')}function c(a){var b=btoa(unescape(encodeURIComponent(JSON.stringify(a))));return'/*# '+('sourceMappingURL=data:application/json;charset=utf-8;base64,'+b)+' */'}a.exports=function(a){var c=[];return c.toString=function(){return this.map(function(c){var d=b(c,a);return c[2]?'@media '+c[2]+'{'+d+'}':d}).join('')},c.i=function(a,b){'string'==typeof a&&(a=[[null,a,'']]);for(var d,e={},f=0;f<this.length;f++)d=this[f][0],'number'==typeof d&&(e[d]=!0);for(f=0;f<a.length;f++){var g=a[f];'number'==typeof g[0]&&e[g[0]]||(b&&!g[2]?g[2]=b:b&&(g[2]='('+g[2]+') and ('+b+')'),c.push(g))}},c}},2:function(a,b,c){function d(a,b){for(var c=0;c<a.length;c++){var d=a[c],e=o[d.id];if(e){e.refs++;for(var f=0;f<e.parts.length;f++)e.parts[f](d.parts[f]);for(;f<d.parts.length;f++)e.parts.push(k(d.parts[f],b))}else{for(var g=[],f=0;f<d.parts.length;f++)g.push(k(d.parts[f],b));o[d.id]={id:d.id,refs:1,parts:g}}}}function e(a,b){for(var c=[],d={},e=0;e<a.length;e++){var f=a[e],g=b.base?f[0]+b.base:f[0],h=f[1],i=f[2],j=f[3],k={css:h,media:i,sourceMap:j};d[g]?d[g].parts.push(k):c.push(d[g]={id:g,parts:[k]})}return c}function f(a,b){var c=q(a.insertInto);if(!c)throw new Error('Couldn\'t find a style target. This probably means that the value for the \'insertInto\' parameter is invalid.');var d=t[t.length-1];if('top'===a.insertAt)d?d.nextSibling?c.insertBefore(b,d.nextSibling):c.appendChild(b):c.insertBefore(b,c.firstChild),t.push(b);else if('bottom'===a.insertAt)c.appendChild(b);else throw new Error('Invalid value for parameter \'insertAt\'. Must be \'top\' or \'bottom\'.')}function g(a){if(null===a.parentNode)return!1;a.parentNode.removeChild(a);var b=t.indexOf(a);0<=b&&t.splice(b,1)}function h(a){var b=document.createElement('style');return a.attrs.type='text/css',j(b,a.attrs),f(a,b),b}function i(a){var b=document.createElement('link');return a.attrs.type='text/css',a.attrs.rel='stylesheet',j(b,a.attrs),f(a,b),b}function j(a,b){Object.keys(b).forEach(function(c){a.setAttribute(c,b[c])})}function k(a,b){var c,d,e,f;if(b.transform&&a.css)if(f=b.transform(a.css),f)a.css=f;else return function(){};if(b.singleton){var j=s++;c=r||(r=h(b)),d=l.bind(null,c,j,!1),e=l.bind(null,c,j,!0)}else a.sourceMap&&'function'==typeof URL&&'function'==typeof URL.createObjectURL&&'function'==typeof URL.revokeObjectURL&&'function'==typeof Blob&&'function'==typeof btoa?(c=i(b),d=n.bind(null,c,b),e=function(){g(c),c.href&&URL.revokeObjectURL(c.href)}):(c=h(b),d=m.bind(null,c),e=function(){g(c)});return d(a),function(b){if(b){if(b.css===a.css&&b.media===a.media&&b.sourceMap===a.sourceMap)return;d(a=b)}else e()}}function l(a,b,c,d){var e=c?'':d.css;if(a.styleSheet)a.styleSheet.cssText=v(b,e);else{var f=document.createTextNode(e),g=a.childNodes;g[b]&&a.removeChild(g[b]),g.length?a.insertBefore(f,g[b]):a.appendChild(f)}}function m(a,b){var c=b.css,d=b.media;if(d&&a.setAttribute('media',d),a.styleSheet)a.styleSheet.cssText=c;else{for(;a.firstChild;)a.removeChild(a.firstChild);a.appendChild(document.createTextNode(c))}}function n(a,b,c){var d=c.css,e=c.sourceMap,f=b.convertToAbsoluteUrls===void 0&&e;(b.convertToAbsoluteUrls||f)&&(d=u(d)),e&&(d+='\n/*# sourceMappingURL=data:application/json;base64,'+btoa(unescape(encodeURIComponent(JSON.stringify(e))))+' */');var g=new Blob([d],{type:'text/css'}),h=a.href;a.href=URL.createObjectURL(g),h&&URL.revokeObjectURL(h)}var o={},p=function(a){var b;return function(){return'undefined'==typeof b&&(b=a.apply(this,arguments)),b}}(function(){return window&&document&&document.all&&!window.atob}),q=function(a){var b={};return function(c){return'undefined'==typeof b[c]&&(b[c]=a.call(this,c)),b[c]}}(function(a){return document.querySelector(a)}),r=null,s=0,t=[],u=c(7);a.exports=function(a,b){if('undefined'!=typeof DEBUG&&DEBUG&&'object'!=typeof document)throw new Error('The style-loader cannot be used in a non-browser environment');b=b||{},b.attrs='object'==typeof b.attrs?b.attrs:{},b.singleton||(b.singleton=p()),b.insertInto||(b.insertInto='head'),b.insertAt||(b.insertAt='bottom');var c=e(a,b);return d(c,b),function(a){for(var f=[],g=0;g<c.length;g++){var h=c[g],i=o[h.id];i.refs--,f.push(i)}if(a){var k=e(a,b);d(k,b)}for(var i,g=0;g<f.length;g++)if(i=f[g],0===i.refs){for(var l=0;l<i.parts.length;l++)i.parts[l]();delete o[i.id]}}};var v=function(){var a=[];return function(b,c){return a[b]=c,a.filter(Boolean).join('\n')}}()},23:function(a,b,c){'use strict';Object.defineProperty(b,'__esModule',{value:!0}),b.completionPrev=b.completionNext=b.setCompletions=b.setConsoleText=b.hideCommand=b.showInfo=b.showError=b.showFind=b.showCommand=void 0;var d=c(24),e=function(a){return a&&a.__esModule?a:{default:a}}(d);b.showCommand=function(a){return{type:e.default.CONSOLE_SHOW_COMMAND,text:a}},b.showFind=function(){return{type:e.default.CONSOLE_SHOW_FIND}},b.showError=function(a){return{type:e.default.CONSOLE_SHOW_ERROR,text:a}},b.showInfo=function(a){return{type:e.default.CONSOLE_SHOW_INFO,text:a}},b.hideCommand=function(){return{type:e.default.CONSOLE_HIDE_COMMAND}},b.setConsoleText=function(a){return{type:e.default.CONSOLE_SET_CONSOLE_TEXT,consoleText:a}},b.setCompletions=function(a,b){return{type:e.default.CONSOLE_SET_COMPLETIONS,completionSource:a,completions:b}},b.completionNext=function(){return{type:e.default.CONSOLE_COMPLETION_NEXT}},b.completionPrev=function(){return{type:e.default.CONSOLE_COMPLETION_PREV}}},24:function(a,b){'use strict';Object.defineProperty(b,'__esModule',{value:!0}),b.default={CONSOLE_SHOW_COMMAND:'console.show.command',CONSOLE_SHOW_ERROR:'console.show.error',CONSOLE_SHOW_INFO:'console.show.info',CONSOLE_HIDE_COMMAND:'console.hide.command',CONSOLE_SET_CONSOLE_TEXT:'console.set.command',CONSOLE_SET_COMPLETIONS:'console.set.completions',CONSOLE_COMPLETION_NEXT:'console.completion.next',CONSOLE_COMPLETION_PREV:'console.completion.prev',CONSOLE_SHOW_FIND:'console.show.find'}},5:function(a,b){'use strict';function c(a,b){if(!(a instanceof b))throw new TypeError('Cannot call a class as a function')}Object.defineProperty(b,'__esModule',{value:!0});var d=function(){function a(a,b){for(var c,d=0;d<b.length;d++)c=b[d],c.enumerable=c.enumerable||!1,c.configurable=!0,'value'in c&&(c.writable=!0),Object.defineProperty(a,c.key,c)}return function(b,c,d){return c&&a(b.prototype,c),d&&a(b,d),b}}(),e=function(){function a(b,d){c(this,a),this.reducer=b,this.catcher=d,this.subscribers=[];try{this.state=this.reducer(void 0,{})}catch(a){d(a)}}return d(a,[{key:'dispatch',value:function(a,b){var c=this;if(a instanceof Promise)a.then(function(d){c.transitNext(d,b)}).catch(function(a){c.catcher(a,b)});else try{this.transitNext(a,b)}catch(a){this.catcher(a,b)}return a}},{key:'getState',value:function(){return this.state}},{key:'subscribe',value:function(a){this.subscribers.push(a)}},{key:'transitNext',value:function(a,b){var c=this.reducer(this.state,a);JSON.stringify(this.state)!==JSON.stringify(c)&&(this.state=c,this.subscribers.forEach(function(a){return a(b)}))}}]),a}(),f=function(){};b.createStore=function(a){var b=1<arguments.length&&arguments[1]!==void 0?arguments[1]:f;return new e(a,b)}},7:function(a){a.exports=function(a){var b='undefined'!=typeof window&&window.location;if(!b)throw new Error('fixUrls requires window.location');if(!a||'string'!=typeof a)return a;var c=b.protocol+'//'+b.host,d=c+b.pathname.replace(/\/[^\/]*$/,'/'),e=a.replace(/url\s*\(((?:[^)(]|\((?:[^)(]+|\([^)(]*\))*\))*)\)/gi,function(a,b){var e=b.trim().replace(/^"(.*)"$/,function(a,b){return b}).replace(/^'(.*)'$/,function(a,b){return b});if(/^(#|data:|http:\/\/|https:\/\/|file:\/\/\/)/i.test(e))return a;var f;return f=0===e.indexOf('//')?e:0===e.indexOf('/')?c+e:d+e.replace(/^\.\//,''),'url('+JSON.stringify(f)+')'});return e}},82:function(a,b,c){'use strict';function d(a){return a&&a.__esModule?a:{default:a}}c(83);var e=c(0),f=d(e),g=c(85),h=d(g),i=c(86),j=d(i),k=c(87),l=d(k),m=c(5),n=c(23),o=function(a){if(a&&a.__esModule)return a;var b={};if(null!=a)for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&&(b[c]=a[c]);return b.default=a,b}(n),p=(0,m.createStore)(l.default);window.addEventListener('load',function(){var a=document.querySelector('#vimvixen-console-completion');new h.default(a,p),new j.default(document.body,p)});var q=function(a){switch(a.type){case f.default.CONSOLE_SHOW_COMMAND:return p.dispatch(o.showCommand(a.command));case f.default.CONSOLE_SHOW_FIND:return p.dispatch(o.showFind());case f.default.CONSOLE_SHOW_ERROR:return p.dispatch(o.showError(a.text));case f.default.CONSOLE_SHOW_INFO:return p.dispatch(o.showInfo(a.text));}};browser.runtime.onMessage.addListener(q),window.addEventListener('message',function(a){q(JSON.parse(a.data))},!1)},83:function(a,b,c){var d=c(84);'string'==typeof d&&(d=[[a.i,d,'']]);var e,f={};f.transform=e;c(2)(d,f);d.locals&&(a.exports=d.locals),!1},84:function(a,b,c){b=a.exports=c(1)(void 0),b.push([a.i,'html, body, * {\n  margin: 0;\n  padding: 0; }\n\nbody {\n  position: absolute;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  overflow: hidden; }\n\n.vimvixen-console {\n  bottom: 0;\n  margin: 0;\n  padding: 0; }\n  .vimvixen-console-command-wrapper {\n    border-top: 1px solid gray; }\n  .vimvixen-console-completion {\n    background-color: white;\n    font-style: normal;\n    font-family: monospace;\n    font-size: 12px;\n    line-height: 16px; }\n    .vimvixen-console-completion-title {\n      background-color: lightgray;\n      font-weight: bold;\n      margin: 0;\n      padding: 0; }\n    .vimvixen-console-completion-item {\n      padding-left: 1.5rem;\n      background-position: 0 center;\n      background-size: contain;\n      background-repeat: no-repeat;\n      white-space: nowrap; }\n      .vimvixen-console-completion-item.vimvixen-completion-selected {\n        background-color: yellow; }\n      .vimvixen-console-completion-item-caption {\n        display: inline-block;\n        width: 40%;\n        text-overflow: ellipsis;\n        overflow: hidden; }\n      .vimvixen-console-completion-item-url {\n        display: inline-block;\n        color: green;\n        width: 60%;\n        text-overflow: ellipsis;\n        overflow: hidden; }\n  .vimvixen-console-message {\n    font-style: normal;\n    font-family: monospace;\n    font-size: 12px;\n    line-height: 16px;\n    border-top: 1px solid gray; }\n  .vimvixen-console-error {\n    background-color: red;\n    font-weight: bold;\n    color: white; }\n  .vimvixen-console-info {\n    background-color: white;\n    font-weight: normal;\n    color: green; }\n  .vimvixen-console-command {\n    background-color: white;\n    display: flex; }\n    .vimvixen-console-command-prompt:before {\n      font-style: normal;\n      font-family: monospace;\n      font-size: 12px;\n      line-height: 16px; }\n    .vimvixen-console-command-prompt.prompt-command:before {\n      content: \':\'; }\n    .vimvixen-console-command-prompt.prompt-find:before {\n      content: \'/\'; }\n    .vimvixen-console-command-input {\n      border: none;\n      flex-grow: 1;\n      font-style: normal;\n      font-family: monospace;\n      font-size: 12px;\n      line-height: 16px; }\n',''])},85:function(a,b){'use strict';function c(a,b){if(!(a instanceof b))throw new TypeError('Cannot call a class as a function')}Object.defineProperty(b,'__esModule',{value:!0});var d=function(){function a(a,b){for(var c,d=0;d<b.length;d++)c=b[d],c.enumerable=c.enumerable||!1,c.configurable=!0,'value'in c&&(c.writable=!0),Object.defineProperty(a,c.key,c)}return function(b,c,d){return c&&a(b.prototype,c),d&&a(b,d),b}}(),e=function(){function a(b,d){var e=this;c(this,a),this.wrapper=b,this.store=d,this.prevState={},d.subscribe(function(){e.update()})}return d(a,[{key:'update',value:function(){var a=this.store.getState();if(JSON.stringify(this.prevState)!==JSON.stringify(a)){this.wrapper.innerHTML='';for(var b=0;b<a.completions.length;++b){var c=a.completions[b],d=this.createCompletionTitle(c.name);this.wrapper.append(d);for(var e=0;e<c.items.length;++e){var f=c.items[e],g=this.createCompletionItem(f.icon,f.caption,f.url);this.wrapper.append(g),b===a.groupSelection&&e===a.itemSelection&&g.classList.add('vimvixen-completion-selected')}}this.prevState=a}}},{key:'createCompletionTitle',value:function(a){var b=this.wrapper.ownerDocument,c=b.createElement('li');return c.className='vimvixen-console-completion-title',c.textContent=a,c}},{key:'createCompletionItem',value:function(a,b,c){var d=this.wrapper.ownerDocument,e=d.createElement('span');e.className='vimvixen-console-completion-item-caption',e.textContent=b;var f=d.createElement('span');f.className='vimvixen-console-completion-item-url',f.textContent=c;var g=d.createElement('li');return g.style.backgroundImage='url('+a+')',g.className='vimvixen-console-completion-item',g.append(e),g.append(f),g}}]),a}();b.default=e},86:function(a,b,c){'use strict';function d(a,b){if(!(a instanceof b))throw new TypeError('Cannot call a class as a function')}Object.defineProperty(b,'__esModule',{value:!0});var e=function(){function a(a,b){for(var c,d=0;d<b.length;d++)c=b[d],c.enumerable=c.enumerable||!1,c.configurable=!0,'value'in c&&(c.writable=!0),Object.defineProperty(a,c.key,c)}return function(b,c,d){return c&&a(b.prototype,c),d&&a(b,d),b}}(),f=c(0),g=function(a){return a&&a.__esModule?a:{default:a}}(f),h=c(23),i=function(a){if(a&&a.__esModule)return a;var b={};if(null!=a)for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&&(b[c]=a[c]);return b.default=a,b}(h),j=function(a){return['command','find'].includes(a.mode)},k=function(){function a(b,c){var e=this;d(this,a),this.wrapper=b,this.store=c,this.prevMode='';var f=this.wrapper.ownerDocument,g=f.querySelector('#vimvixen-console-command-input');g.addEventListener('blur',this.onBlur.bind(this)),g.addEventListener('keydown',this.onKeyDown.bind(this)),g.addEventListener('input',this.onInput.bind(this)),c.subscribe(function(){e.update()}),this.update()}return e(a,[{key:'onBlur',value:function(){var a=this.store.getState();'command'===a.mode&&this.hideCommand()}},{key:'doEnter',value:function(a){return a.stopPropagation(),a.preventDefault(),this.onEntered(a.target.value)}},{key:'selectNext',value:function(a){this.store.dispatch(i.completionNext()),a.stopPropagation(),a.preventDefault()}},{key:'selectPrev',value:function(a){this.store.dispatch(i.completionPrev()),a.stopPropagation(),a.preventDefault()}},{key:'onKeyDown',value:function(a){switch(a.keyCode){case KeyboardEvent.DOM_VK_ESCAPE:return this.hideCommand();case KeyboardEvent.DOM_VK_RETURN:return this.doEnter(a);case KeyboardEvent.DOM_VK_TAB:a.shiftKey?this.store.dispatch(i.completionPrev()):this.store.dispatch(i.completionNext()),a.stopPropagation(),a.preventDefault();break;case KeyboardEvent.DOM_VK_OPEN_BRACKET:if(a.ctrlKey)return this.hideCommand();break;case KeyboardEvent.DOM_VK_M:if(a.ctrlKey)return this.doEnter(a);break;case KeyboardEvent.DOM_VK_N:a.ctrlKey&&this.selectNext(a);break;case KeyboardEvent.DOM_VK_P:a.ctrlKey&&this.selectPrev(a);}}},{key:'onEntered',value:function(a){var b=this.store.getState();'command'===b.mode?(browser.runtime.sendMessage({type:g.default.CONSOLE_ENTER_COMMAND,text:a}),this.hideCommand()):'find'===b.mode&&(this.hideCommand(),window.top.postMessage(JSON.stringify({type:g.default.CONSOLE_ENTER_FIND,text:a}),'*'))}},{key:'onInput',value:function(a){var b=this;this.store.dispatch(i.setConsoleText(a.target.value));var c=a.target.value;return browser.runtime.sendMessage({type:g.default.CONSOLE_QUERY_COMPLETIONS,text:c}).then(function(a){b.store.dispatch(i.setCompletions(c,a))})}},{key:'onInputShown',value:function(a){var b=this.wrapper.ownerDocument,c=b.querySelector('#vimvixen-console-command-input');c.focus(),window.focus(),'command'===a.mode&&this.onInput({target:c})}},{key:'hideCommand',value:function(){this.store.dispatch(i.hideCommand()),window.top.postMessage(JSON.stringify({type:g.default.CONSOLE_UNFOCUS}),'*')}},{key:'update',value:function(){var a=this.store.getState();this.updateMessage(a),this.updateCommand(a),this.updatePrompt(a),this.prevMode!==a.mode&&j(a)&&this.onInputShown(a),this.prevMode=a.mode}},{key:'updateMessage',value:function(a){var b=this.wrapper.ownerDocument,c=b.querySelector('.vimvixen-console-message'),d='none',e=['vimvixen-console-message'];('error'===a.mode||'info'===a.mode)&&(d='block',e.push('vimvixen-console-'+a.mode)),c.className=e.join(' '),c.style.display=d,c.textContent=a.messageText}},{key:'updateCommand',value:function(a){var b=this.wrapper.ownerDocument,c=b.querySelector('#vimvixen-console-command'),d=b.querySelector('#vimvixen-console-command-input'),e='none';j(a)&&(e='block'),c.style.display=e,d.value=a.consoleText}},{key:'updatePrompt',value:function(a){var b=['vimvixen-console-command-prompt'];j(a)&&b.push('prompt-'+a.mode);var c=this.wrapper.ownerDocument,d=c.querySelector('.vimvixen-console-command-prompt');d.className=b.join(' ')}}]),a}();b.default=k},87:function(a,b,c){'use strict';Object.defineProperty(b,'__esModule',{value:!0}),b.default=function(){var a=0<arguments.length&&arguments[0]!==void 0?arguments[0]:f,b=1<arguments.length&&arguments[1]!==void 0?arguments[1]:{};switch(b.type){case e.default.CONSOLE_SHOW_COMMAND:return Object.assign({},a,{mode:'command',consoleText:b.text,completions:[]});case e.default.CONSOLE_SHOW_FIND:return Object.assign({},a,{mode:'find',consoleText:'',completions:[]});case e.default.CONSOLE_SHOW_ERROR:return Object.assign({},a,{mode:'error',messageText:b.text});case e.default.CONSOLE_SHOW_INFO:return Object.assign({},a,{mode:'info',messageText:b.text});case e.default.CONSOLE_HIDE_COMMAND:return Object.assign({},a,{mode:'command'===a.mode||'find'===a.mode?'':a.mode});case e.default.CONSOLE_SET_CONSOLE_TEXT:return Object.assign({},a,{consoleText:b.consoleText});case e.default.CONSOLE_SET_COMPLETIONS:return Object.assign({},a,{completions:b.completions,completionSource:b.completionSource,groupSelection:-1,itemSelection:-1});case e.default.CONSOLE_COMPLETION_NEXT:{var c=g(a);return Object.assign({},a,{groupSelection:c[0],itemSelection:c[1],consoleText:i(a.completions,c[0],c[1],a.completionSource)})}case e.default.CONSOLE_COMPLETION_PREV:{var d=h(a);return Object.assign({},a,{groupSelection:d[0],itemSelection:d[1],consoleText:i(a.completions,d[0],d[1],a.completionSource)})}default:return a;}};var d=c(24),e=function(a){return a&&a.__esModule?a:{default:a}}(d),f={mode:'',messageText:'',consoleText:'',completionSource:'',completions:[],groupSelection:-1,itemSelection:-1},g=function(a){if(0>a.groupSelection)return[0,0];var b=a.completions[a.groupSelection];return a.groupSelection+1>=a.completions.length&&a.itemSelection+1>=b.items.length?[-1,-1]:a.itemSelection+1>=b.items.length?[a.groupSelection+1,0]:[a.groupSelection,a.itemSelection+1]},h=function(a){if(0>a.groupSelection)return[a.completions.length-1,a.completions[a.completions.length-1].items.length-1];return 0===a.groupSelection&&0===a.itemSelection?[-1,-1]:0===a.itemSelection?[a.groupSelection-1,a.completions[a.groupSelection-1].items.length-1]:[a.groupSelection,a.itemSelection-1]},i=function(a,b,c,d){return 0>b||0>c?d:a[b].items[c].content}}});