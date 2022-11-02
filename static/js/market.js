document.addEventListener('DOMContentLoaded', () => {
  const prevButton = document.querySelector('#prev-btn');
  const nextButton = document.querySelector('#next-btn');

  const url = new URL(window.location);
  if (!url.searchParams.get('page')) {
    initQueryParam(url);
  }

  nextButton.addEventListener('click', async () => {
    const pageNumber = parseInt(url.searchParams.get('page')) + 1;
    await getProducts(pageNumber);
    url.searchParams.set('page', pageNumber);
    window.history.pushState({}, '', url);
  });

  prevButton.addEventListener('click', async () => {
    const pageNumber = parseInt(url.searchParams.get('page')) - 1;
    await getProducts(pageNumber);
    url.searchParams.set('page', pageNumber);
    window.history.pushState({}, '', url);
  });

  getProducts(parseInt(url.searchParams.get('page')));
});

const initQueryParam = (url) => {
  url.searchParams.set('page', 1);
  window.history.pushState({}, '', url);
};

const getProducts = async (pageNumber) => {
  const cardContainer = document.querySelector('#cards-container');
  const currentPage = document.querySelector('#current-page');
  const numberPages = document.querySelector('#number-pages');
  const prevButton = document.querySelector('#prev-btn');
  const nextButton = document.querySelector('#next-btn');

  const response = await fetch(`/market/product?page=${pageNumber}`);
  const data = await response.json();

  const {
    totalPages,
    products,
    meta: { hasNextPage, hasPrevPage },
  } = data.content;

  currentPage.innerHTML = pageNumber;
  numberPages.innerHTML = totalPages;

  if (!hasNextPage) {
    nextButton.classList.add('hidden');
  } else {
    nextButton.classList.remove('hidden');
  }

  if (!hasPrevPage) {
    prevButton.classList.add('hidden');
  } else {
    prevButton.classList.remove('hidden');
  }

  if (data.success) {
    cardContainer.innerHTML = '';
    products.map((product) => {
      cardContainer.innerHTML += `<div
      id="${product.id}"
      class="gap-4 flex flex-col w-full shadow-md border-[16px] border-white rounded-xl"
    >
      <div class="flex items-center grow">
        <img src="${product.image}" class="rounded-xl" />
      </div>
      <div class="h-max">
        <span class="font-['Montserrat'] font-bold text-base">
            ${product.name}
        </span>
        <div class="font-['Montserrat'] flex items-center gap-2">
          <span class="text-[#56C969] font-bold">${product.stock}</span
          ><span> remaining</span>
        </div>
        <div class="flex flex-row gap-4 pb-[16px] items-center">
          <button
            onclick="sub(${product.id})"
            class="text-2xl grow text-right text-[#56C969] font-['Montserrat'] font-bold"
          >
            -
          </button>
          <object
            id="count-${product.id}"
            class="grow-0 font-['Montserrat']"
          >
            0
          </object>
          <button
            onclick="add(${product.id}, ${product.stock})"
            class="text-2xl grow text-left font-['Montserrat'] text-[#56C969] font-bold"
          >
            +
          </button>
        </div>
        <div class="flex md:flex-row flex-col items-center gap-2">
          <div class="flex md:w-1/2 gap-2 w-full md:justify-start justify-center">
            <img src="/static/images/coin.png" />
            <span class="font-bold">${product.price}</span>
          </div>
          <div class="grow md:w-1/2 w-full">
            <button class="w-full text-white button-primary">BUY</button>
          </div>
        </div>
      </div>
    </div>`;
    });
  }
};
