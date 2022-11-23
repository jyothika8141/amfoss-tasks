use std::error::Error;
use csv::Writer;

fn main() -> Result<(), Box<dyn Error>>{

    let response = reqwest::blocking::get(
        "https://crypto.com/price")
    .unwrap()
    .text()
    .unwrap();
    let document = scraper::Html::parse_document(&response);
        
    let names_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let names = document.select(&names_selector).map(|x| x.inner_html());

    let price_selector = scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let price = document.select(&price_selector).map(|x| x.inner_html());

    let change24_selector = scraper::Selector::parse("td.css-1b7j986>p").unwrap();
    let change24 = document.select(&change24_selector).map(|x| x.inner_html());

    let volume24_market_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let volume24_market = document.select(&volume24_market_selector).map(|x| x.inner_html());
    
   
    let mut v_names = vec![];
    let mut v_price = vec![];
    let mut v_change24 = vec![];
    let mut v_volume24_market = vec![];

    names
        .for_each(|item| v_names.push(item));
    
    price
        .for_each(|item| v_price.push(item));

    change24
        .for_each(|item| v_change24.push(item));
    
    volume24_market
        .for_each(|item| v_volume24_market.push(item));

    let mut wtr = Writer::from_path("cryptocurrency.csv")?;
    wtr.write_record(&["NAME", "PRICE", "24H CHANGE", "24H VOLUME", "MARKET CAP"]);
    for i in 0..50{
        wtr.write_record(&[v_names[i].clone(), v_price[i].clone(), v_change24[i].clone(), v_volume24_market[i*2].clone(), v_volume24_market[i*2+1].clone()]);
    }
    wtr.flush()?;
    Ok(())
}


