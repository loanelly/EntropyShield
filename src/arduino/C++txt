// ============================================================================
// PROJECT: LNL-EntropyShield (True Random Number Generator)
// ORGANIZATION: LNL-Engineering (https://github.com/LNL-Engineering)
// ============================================================================
/* 
==============================================================================
[EN] WHY DO WE NEED THIS TOGGLE (WOKWI_EMULATION_MODE)?
Wokwi is a pure digital simulator. In a virtual environment, an unconnected analog 
pin or timer runs on deterministic math, resulting in predictable patterns (like 
repeating 0x55 or 0xAA bytes). Real physical entropy (thermal/shot noise of a p-n 
junction) cannot be simulated. 

- Set to 'true' (Wokwi Mode): Uses a software-generated random bit source to pass 
  through the Von Neumann filter, preventing infinite loops and ensuring active output.
- Set to 'false' (Production Mode): Disables software crutches. The code relies 
  strictly on the true quantum randomness of a real hardware transistor noise generator.

==============================================================================
[RU] ЗАЧЕМ НУЖЕН ЭТОТ ПЕРЕКЛЮЧАТЕЛЬ (WOKWI_EMULATION_MODE)?
Симулятор Wokwi имеет чисто цифровую природу. В виртуальной среде неподключенный 
аналоговый пин или таймер работают по строгим математическим формулам, что приводит 
к циклическим повторам или зависанию алгоритма фон Неймана в бесконечном цикле. 
Реальную физическую энтропию (тепловой шум транзистора) невозможно смоделировать программно.

- Режим 'true' (Для Wokwi): Подает на вход фильтра фон Неймана программные случайные 
  биты, что предотвращает зависание симулятора и оживляет монитор порта.
- Режим 'false' (Для реального железа): Полностью отключает программные "костыли". 
  Код опирается исключительно на истинный квантовый хаос физического транзистора.
==============================================================================
*/
// TOGGLE SWITCH / ПЕРЕКЛЮЧАТЕЛЬ РЕЖИМОВ
// Set to true for Wokwi simulation. Set to false for real hardware assembly.
#define WOKWI_EMULATION_MODE true 

const int noisePin = A0;

void setup() {
  Serial.begin(115200);
  pinMode(noisePin, INPUT);
  
  if (WOKWI_EMULATION_MODE) {
    randomSeed(analogRead(A1) + micros());
  } else {
    ADCSRA &= ~(1 << ADPS2); 
    TCCR0A = 0;
    TCCR0B = _BV(CS00); 
  }
}

int getTrueRandomBit() {
  while (true) {
    int bit1, bit2;

    if (WOKWI_EMULATION_MODE) {
      bit1 = random(0, 2); 
      bit2 = random(0, 2);
    } else {
      bit1 = (analogRead(noisePin) ^ TCNT0) & 1;
      delayMicroseconds(37); 
      bit2 = (analogRead(noisePin) ^ TCNT0) & 1;
      delayMicroseconds(37);
    }

    if (bit1 == 1 && bit2 == 0) return 1;
    if (bit1 == 0 && bit2 == 1) return 0;
  }
}

byte getTrueRandomByte() {
  byte randomByte = 0;
  for (int i = 0; i < 8; i++) {
    randomByte = (randomByte << 1) | getTrueRandomBit();
  }
  return randomByte;
}

void loop() {
  byte secretByte = getTrueRandomByte();
  
  if (secretByte < 16) Serial.print("0");
  Serial.print(secretByte, HEX);
  Serial.print(" "); 
  
  delay(15); 
}
