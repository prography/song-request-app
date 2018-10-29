(function () {
  const root = document.querySelector('.app-root');

  const empty = document.body;

  function renderHtml(html) {
    root.innerHTML = html;
  }

  function guestRender(html) {
    empty.innerHTML = html;
  }

  function get(url) {
    return new Promise((resolve, reject) => {
      const req = new XMLHttpRequest();
      req.open('GET', url);
      req.send();

      req.onreadystatechange = function () {
        if (req.readyState === XMLHttpRequest.DONE) {
          if (req.status === 200) resolve(req.response);
          else reject(req.statusText);
        }
      };
    });
  }

  function setURL(url) {
      location.href = url + '.html';
  }

  const routes = {
    '': function () {
      get('/data/host-home-window.html').then(renderHtml);
    },
    'end': function () {
      get('/data/host-end-request-window.html').then(renderHtml);
    },
    'settings': function () {
      get('/data/host-setting-window.html').then(renderHtml);
    },
    'empty': function () {
      get('/data/host-empty-window.html').then(renderHtml);
    },
    'guest-start': function () {
      get('/data/guest-request-start-window.html').then(guestRender);
    },
    'guest-end': function () {
      get('/data/guest-request-end-window.html').then(guestRender);
    },
    otherwise() {
      root.innerHTML = `${location.hash} Not Found`;
    }
  };

  function router() {
    // url의 hash를 취득
    const hash = location.hash.replace('#', '');
    (routes[hash] || routes.otherwise)();
  }

  // 네비게이션을 클릭하면 uri의 hash가 변경된다. 주소창의 uri가 변경되므로 history 관리가 가능하다.
  // 이때 uri의 hash만 변경되면 서버로 요청을 수행하지 않는다.
  // 따라서 uri의 hash가 변경하면 발생하는 이벤트인 hashchange 이벤트를 사용하여 hash의 변경을 감지하여 필요한 AJAX 요청을 수행한다.
  // hash 방식의 단점은 uri에 불필요한 #이 들어간다는 것이다.
  window.addEventListener('hashchange', router);

  // DOMContentLoaded은 HTML과 script가 로드된 시점에 발생하는 이벤트로 load 이벤트보다 먼저 발생한다. (IE 9 이상 지원)
  // 새로고침이 클릭되었을 때, 웹페이지가 처음 로딩되었을 때, 현 페이지(예를들어 loclahost:5003/#service)를 요청하므로 index.html이 재로드되고 DOMContentLoaded 이벤트가 발생하여 router가 호출된다.
  window.addEventListener('DOMContentLoaded', router);
}());
